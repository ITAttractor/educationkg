import json
import datetime
from ntc.models import ParsedNTC


class NTCDataSaver(object):
    def __init__(self, json):
        self.data = None
        self.json = json
        self.objects_to_save = []

    def load(self):
        self._convert_json()
        self._add_records()

    def _convert_json(self):
        self.data = json.loads(self.json)

    def _add_records(self):
        for item in self.data:
            self._add_record(item)
        ParsedNTC.objects.bulk_create(self.objects_to_save)

    def _add_record(self, item):
        location = item['location']
        for school in item['schools']:
            school_title = school['title']
            for result in school['results']:
                ntc = ParsedNTC()
                ntc.location = location
                ntc.school_title = school_title
                ntc.full_name = result['full_name']
                ntc.math = result['math']
                ntc.physics = result['physics']
                ntc.chemistry = result['chemistry']
                ntc.geometry = result['geometry']
                ntc.biology = result['biology']
                ntc.geography = result['geography']
                ntc.history = result['history']
                ntc.eng_lang = result['eng_lang']
                ntc.ger_lang = result['ger_lang']
                ntc.fr_lang = result['fr_lang']
                ntc.kyr_lang = result['kyr_lang']
                ntc.rus_lang = result['rus_lang']
                ntc.uzb_lang = result['uzb_lang']
                ntc.informatics = result['informatics']
                ntc.civics = result['civics']
                ntc.notes = result['notes']
                self.objects_to_save.append(ntc)
