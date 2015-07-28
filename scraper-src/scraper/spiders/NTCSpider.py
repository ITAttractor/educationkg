# coding=utf-8
import urlparse
import re
import requests
from scraper.items import School, Result, Location
from scrapy import Selector
from scrapy.http.request import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import lxml.html

TD_WITH_CLASS_XPATH = "//td[contains(@class, '%s')]"
SCHOOL_SELECTOR_GROUP_NAME = "school_selector_name"
IFRAME_SRC_XPATH = "//iframe/@src"
URL_GROUP_NAME = 'url'
PARSED_PAGE_WITH_DOCUMENT_PATTERN = "RefreshParent\(\'(?P<%s>.*)\'\)"

SCHOOL_CSS_SELECTOR_PATTERN = r"\.(?P<%s>.*)\{font:\sitalic\sbold\s\b13px"
UNNECESSARY_TD_PATTERN = r"\.(?P<td_skip_class>td\d{1,3})\{.*width:\s([1-9]|1[0-5])px"

ELEVENTH_CLASS_PDF_LINKS_XPATH = "//div[@id='content']//a[contains(text(), '11')]"
RESULTS_TR_XPATH = ".//table//td[p/text() >= 1]/.."
SCHOOL_TITLE_XPATH = "(./preceding::*[contains(@class, '%s')])[last()]/descendant-or-self::*/text()"

RESULT_TABLE_XPATH = "./td[%d]/descendant-or-self::*/text()"
FULL_NAME_TD_ID = 2
MATH_TD_ID = 3
PHYSICS_TD_ID = 4
CHEMISTRY_TD_ID = 5
GEOMETRY_TD_ID = 6
BIOLOGY_TD_ID = 7
GEOGRAPHY_TD_ID = 8
HISTORY_TD_ID = 9
ENG_LANG_TD_ID = 10
GER_LANG_TD_ID = 11
FR_LANG_TD_ID = 12
KYR_LANG_TD_ID = 13
RUS_LANG_TD_ID = 14
UZB_LANG_TD_ID = 15
INFORMATICS_TD_ID = 16
CIVICS_TD_ID = 17
NOTES_TD_ID = 18

NBSP = u' '


class SchoolItemContainer(object):
    def __init__(self):
        self.items = []

    def get_or_create_item_with_title(self, title):
        if self.items:
            school_item = self._get_or_create_school_item_with_title_if_list_not_empty(title)
        else:
            school_item = self._create_school_item_with_title(title)
        return school_item

    def _get_or_create_school_item_with_title_if_list_not_empty(self, title):
        for item in self.items:
            if unicode(item['title']) == unicode(title):
                return item
        school_item = self._create_school_item_with_title(title)
        return school_item

    def _create_school_item_with_title(self, title):
        school_item = School()
        school_item['title'] = title
        school_item['results'] = []
        self.items.append(school_item)
        return school_item

    def get_all_schools(self):
        return self.items


class ResultExtractor(object):
    def __init__(self):
        self.school_item_container = SchoolItemContainer()
        self.selector = None
        self.school_css_selector = None

    def get_results_by_school(self):
        self._get_results()
        results_by_school = self.school_item_container.get_all_schools()
        return results_by_school

    def _get_results(self):
        results = self.selector.xpath(RESULTS_TR_XPATH)
        for result in results:
            result_item = Result()
            school_title = " ".join(result.xpath(SCHOOL_TITLE_XPATH % self.school_css_selector).extract()).replace(u"Школа", "").replace(":", "").strip()
            school_item = self.school_item_container.get_or_create_item_with_title(school_title)
            result_item['full_name'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % FULL_NAME_TD_ID)
            result_item['math'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % MATH_TD_ID)
            result_item['physics'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % PHYSICS_TD_ID)
            result_item['chemistry'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % CHEMISTRY_TD_ID)
            result_item['geometry'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % GEOMETRY_TD_ID)
            result_item['biology'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % BIOLOGY_TD_ID)
            result_item['geography'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % GEOGRAPHY_TD_ID)
            result_item['history'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % HISTORY_TD_ID)
            result_item['eng_lang'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % ENG_LANG_TD_ID)
            result_item['ger_lang'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % GER_LANG_TD_ID)
            result_item['fr_lang'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % FR_LANG_TD_ID)
            result_item['kyr_lang'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % KYR_LANG_TD_ID)
            result_item['rus_lang'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % RUS_LANG_TD_ID)
            result_item['uzb_lang'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % UZB_LANG_TD_ID)
            result_item['informatics'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % INFORMATICS_TD_ID)
            result_item['civics'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % CIVICS_TD_ID)
            result_item['notes'] = self._get_result_table_value(result, RESULT_TABLE_XPATH % NOTES_TD_ID)
            school_item['results'].append(result_item)

    def _get_result_table_value(self, result, xpath):
        value = result.xpath(xpath).extract_first()
        if value == NBSP:
            return None
        else:
            return value.split("/")[0]



class NTCSpider(CrawlSpider):
    name = 'ntc'
    start_urls = [
        "http://ntc.kg/"
    ]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=(ELEVENTH_CLASS_PDF_LINKS_XPATH), deny_extensions=[]), callback="process_pdf"),
    )

    def process_pdf(self, response):
        self.logger.debug("Processing PDF")
        response = self.convert_pdf(response)
        selector = Selector(text=response.content)
        script_with_link = selector.xpath("(//script)[last()]/text()").extract_first()
        match = re.search(PARSED_PAGE_WITH_DOCUMENT_PATTERN % URL_GROUP_NAME, script_with_link)
        url = match.group(URL_GROUP_NAME)
        self.logger.debug("PDF converted")
        yield Request(url=url, callback=self.parse_iframe)

    def convert_pdf(self, response):
        pdf = response.body
        files = {"file": ('ntc.pdf', pdf, 'application/pdf')}
        response = requests.post('http://pdftoword4.pdfonline.com/PDF2WORDWebAppMem/Default-dialogad.aspx?op=upload',
                                 files=files)
        return response

    def parse_iframe(self, response):
        self.logger.debug("Parsing iframe")
        selector = Selector(response=response)
        parsed_url = urlparse.urlparse(response.url)
        iframe_content_path = selector.xpath(IFRAME_SRC_XPATH).extract_first()

        url = "{uri.scheme}://{uri.netloc}{path}".format(uri=parsed_url, path=iframe_content_path)
        yield (Request(url=url, callback=self.parse_ntc))

    def parse_ntc(self, response):
        self.logger.debug("Parsing NTC")
        location_item = Location()
        location_item['title'] = None

        result_extractor = ResultExtractor()
        match = re.search(SCHOOL_CSS_SELECTOR_PATTERN % SCHOOL_SELECTOR_GROUP_NAME, response.body)
        result_extractor.school_css_selector = match.group(SCHOOL_SELECTOR_GROUP_NAME)

        cleaned_html = self.get_cleaned_html(response)
        selector = Selector(text=cleaned_html)
        result_extractor.selector = selector

        location_item['schools'] = result_extractor.get_results_by_school()

        yield location_item


    def get_cleaned_html(self, response):
        td_skip_classes = [set_item[0] for set_item in re.findall(UNNECESSARY_TD_PATTERN, response.body)]
        tree = lxml.html.fromstring(response.body)
        for td_class in td_skip_classes:
            for td in tree.xpath(TD_WITH_CLASS_XPATH % td_class):
                td.getparent().remove(td)
        cleaned_html = lxml.html.tostring(tree, pretty_print=True)
        return cleaned_html
