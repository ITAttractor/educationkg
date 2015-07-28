# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import json
import requests
from scraper.settings import API_KEY, BASE_URL
from scraper.spiders import BillSpider
from scraper.spiders.DeputySpider import DeputySpider
from scraper.spiders.FactionSpider import FactionSpider
from scraper.spiders.SkipSpider import SkipSpider
from scraper.spiders.VoteSpider import VoteSpider
from scrapy.utils.serialize import ScrapyJSONEncoder


url_hash = {
    FactionSpider: BASE_URL + "/api/factions",
    DeputySpider: BASE_URL + "/api/deputies",
    BillSpider: BASE_URL + "/api/bills",
    SkipSpider: BASE_URL + "/api/skips",
    VoteSpider: BASE_URL + "/api/votes"
}


class ScraperPipeline(object):
    def __init__(self):
        self.logger = logging.getLogger("ScraperPipeline")

    def process_item(self, item, spider):
        self.items.append(item)

    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        encoder = ScrapyJSONEncoder()
        self.data = encoder.encode(self.items)
        self.send_data(url_hash[spider.__class__])

    def send_data(self, url):
        response = requests.post(url, data=self.data, headers={'Content-Type': 'application/json', 'AUTHORIZATION': API_KEY})
        self.process_response(response)

    def process_response(self, response):
        if response.status_code == 200:
            self.process_success_response(response)
        else:
            self.process_error_status_code(response)

    def process_error_status_code(self, response):
        self.logger.warning("Content post error, http status code: {0}".format(response.status_code))

    def process_success_response(self, response):
        parsed_content = json.loads(response.content)
        if parsed_content["status"] == "fail":
            self.logger.warning("Content post error")
        else:
            self.logger.info("Content post successfully")


