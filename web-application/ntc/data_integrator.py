# coding=utf-8
from django.db.models import Q
from geo.models import Region, District
from ntc.models import NTC
from schools.models import School


class Searcher(object):
    def __init__(self, location_text, school_title_text):
        self.location_text = location_text
        self.school_title_text = school_title_text

    def _search_for_district(self):
        region = self.search_for_region()

        filtered_districts = District.objects.filter(region=region)
        for district in filtered_districts:
            if district.title in self.location_text:
                return district

    def search_for_region(self):
        for region in Region.objects.all():
            if region.title in self.location_text:
                return region

    def search_for_school(self):
        district = self._search_for_district()
        schools = School.objects.filter(district=district)

        school_title_parts = self.school_title_text.replace(u"№", "").split(" ")
        # http://stackoverflow.com/questions/7088173/how-to-query-model-where-name-contains-any-word-in-python-list
        filtered_schools = schools.filter(reduce(lambda x, y: x | y, [Q(title__contains=part) for part in school_title_parts]))
        return filtered_schools.first()


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
            ntc.math = item.math
            ntc.physics = item.physics
            ntc.chemistry = item.chemistry
            ntc.geometry = item.geometry
            ntc.biology = item.biology
            ntc.geography = item.geography
            ntc.history = item.history
            ntc.eng_lang = item.eng_lang
            ntc.ger_lang = item.ger_lang
            ntc.fr_lang = item.fr_lang
            ntc.kyr_lang = item.kyr_lang
            ntc.rus_lang = item.rus_lang
            ntc.uzb_lang = item.uzb_lang
            ntc.informatics = item.informatics
            ntc.civics = item.civics
            ntc.notes = item.notes
            ntc.parsed_ntc = item
            self.ntc_objects_to_save.append(ntc)
        else:
            self.integrated = False
