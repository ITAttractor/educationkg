# coding=utf-8
from geo.models import Region, District
from ntc.models import NTC
from schools.models import School
import operator


def convert_to_integer(value):
    try:
        return int(value)
    except TypeError:
        return None
    except ValueError:
        return None


def part_with_length_more_than_one_or_part_numberic(part):
    return len(part) > 1 or part.isdigit()


def school_number_in_title_equals_numeric_part(school_title, part):
    return part.isdigit() and part == filter(unicode.isdigit, school_title)


def school_title_contains_non_numeric_part(school_title, part):
    return not part.isdigit() and part in school_title


class Searcher(object):
    def __init__(self, location_text, school_title_text):
        self.location_text = location_text
        self.school_title_text = school_title_text
        self.region = None
        self.district = None
        self.filtered_schools = {}

    def _search_for_district(self):
        filtered_districts = District.objects.filter(region=self.region)
        for district in filtered_districts:
            if district.title in self.location_text:
                self.district = district

    def _search_for_region(self):
        for region in Region.objects.all():
            if region.title in self.location_text:
                self.region = region

    def search_for_school(self):
        self._search_for_region()
        self._search_for_district()
        self._filter_schools()

        return self._get_school_from_filtered()

    def _filter_schools(self):
        schools = School.objects.filter(district=self.district)

        school_title_parts = self._split_and_clean_school_title()

        for school in schools:
            match_count = 0
            for part in school_title_parts:
                if part_with_length_more_than_one_or_part_numberic(part):
                    if school_number_in_title_equals_numeric_part(school.title, part):
                        # has more weight if match by school number
                        match_count += 5
                    elif school_title_contains_non_numeric_part(school.title, part):
                        match_count += 1

            if match_count > 0:
                self.filtered_schools[school] = match_count

    def _get_school_from_filtered(self):
        if self.filtered_schools:
            return self._get_school_with_maximum_match_count()

    def _get_school_with_maximum_match_count(self):
        return max(self.filtered_schools.iteritems(), key=operator.itemgetter(1))[0]

    def _split_and_clean_school_title(self):
        return self.school_title_text.replace(u"№", "")\
            .replace("-", ' ')\
            .replace('.', ' ')\
            .replace('"', '')\
            .split(" ")


class DataIntegrator(object):
    def __init__(self, integration_queue):
        self.integration_queue = integration_queue
        self.ntc_objects_to_save = []
        self.integrated = True

    def integrate(self):
        parsed_ntc_objects = self.integration_queue.parsedntc_set.filter(ntc__isnull=True)

        for item in parsed_ntc_objects:
            self._prepare_object(item)

        NTC.objects.bulk_create(self.ntc_objects_to_save)
        self.save_queue_status()

    def save_queue_status(self):
        self.integration_queue.status = self.integrated
        self.integration_queue.save()

    def _prepare_object(self, item):
        searcher = Searcher(item.location, item.school_title)
        school = searcher.search_for_school()
        if school:
            ntc = NTC()
            ntc.school = school
            ntc.full_name = item.full_name
            ntc.math = convert_to_integer(item.math)
            ntc.physics = convert_to_integer(item.physics)
            ntc.chemistry = convert_to_integer(item.chemistry)
            ntc.geometry = convert_to_integer(item.geometry)
            ntc.biology = convert_to_integer(item.biology)
            ntc.geography = convert_to_integer(item.geography)
            ntc.history = convert_to_integer(item.history)
            ntc.eng_lang = convert_to_integer(item.eng_lang)
            ntc.ger_lang = convert_to_integer(item.ger_lang)
            ntc.fr_lang = convert_to_integer(item.fr_lang)
            ntc.kyr_lang = convert_to_integer(item.kyr_lang)
            ntc.rus_lang = convert_to_integer(item.rus_lang)
            ntc.uzb_lang = convert_to_integer(item.uzb_lang)
            ntc.informatics = convert_to_integer(item.informatics)
            ntc.civics = convert_to_integer(item.civics)
            ntc.notes = item.notes
            ntc.parsed_ntc = item
            self.ntc_objects_to_save.append(ntc)
        else:
            self.integrated = False
