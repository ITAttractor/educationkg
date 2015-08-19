from django.db.models import Avg
from ntc.models import NTC

CIVICS = 'civics'
INFORMATICS = 'informatics'
UZB_LANG = 'uzb_lang'
RUS_LANG = 'rus_lang'
KYR_LANG = 'kyr_lang'
FR_LANG = 'fr_lang'
GER_LANG = 'ger_lang'
ENG_LANG = 'eng_lang'
HISTORY = 'history'
GEOGRAPHY = 'geography'
BIOLOGY = 'biology'
GEOMETRY = 'geometry'
CHEMISTRY = 'chemistry'
PHYSICS = 'physics'
MATH = 'math'


class CalculatedAverages(object):
    def __init__(self):
        self.for_country = []
        self.for_school = []
        self.subjects = []

    def get_school_averages(self):
        return self.for_school

    def get_country_averages(self):
        return self.for_country

    def get_subjects(self):
        return self.subjects

    def add_school_average(self, value):
        self.for_school.append(value)

    def add_country_average(self, value):
        self.for_country.append(value)

    def add_subject(self, value):
        self.subjects.append(value)


class AverageResultsCalculator(object):
    def __init__(self, school):
        self.school = school
        self.average_results_for_school = None
        self.average_results_for_country = None
        self.calculated_averages = CalculatedAverages()

    def _calculate_averages(self, objects):
        return objects.aggregate(
            math=Avg(MATH),
            physics=Avg(PHYSICS),
            chemistry=Avg(CHEMISTRY),
            geometry=Avg(GEOMETRY),
            biology=Avg(BIOLOGY),
            geography=Avg(GEOGRAPHY),
            history=Avg(HISTORY),
            eng_lang=Avg(ENG_LANG),
            ger_lang=Avg(GER_LANG),
            fr_lang=Avg(FR_LANG),
            kyr_lang=Avg(KYR_LANG),
            rus_lang=Avg(RUS_LANG),
            uzb_lang=Avg(UZB_LANG),
            informatics=Avg(INFORMATICS),
            civics=Avg(CIVICS)
        )

    def _calculate_averages_for_country(self):
        all_ntc_objects = NTC.objects.all()
        self.average_results_for_country = self._calculate_averages(all_ntc_objects)

    def _calculate_averages_for_school(self):
        school_ntc_objects = NTC.objects.filter(school=self.school)
        self.average_results_for_school = self._calculate_averages(school_ntc_objects)

    def calculate(self):
        self._calculate_averages_for_country()
        self._calculate_averages_for_school()

        self._prepare_results()

        return self.calculated_averages

    def _prepare_results(self):
        for key, value in self.average_results_for_school.items():
            if value:
                subject = unicode(NTC._meta.get_field_by_name(key)[0].verbose_name)
                self.calculated_averages.add_subject(subject)
                self.calculated_averages.add_school_average(value)
                self.calculated_averages.add_country_average(self.average_results_for_country[key])

    def _get_average_results_for_school(self):
        return self.average_results_for_school

    def _get_average_results_for_country(self):
        return self.average_results_for_school

