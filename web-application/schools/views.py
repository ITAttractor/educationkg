import json
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from ntc.average_results_calculator import AverageResultsCalculator
from ntc.models import NTC
from schools.models import School


class SchoolSearchView(ListView):
    template_name = 'schools/partial_list_on_main_page.html'
    model = School
    paginate_by = 10
    context_object_name = 'schools'

    def get_queryset(self):
        query = self._get_query()
        return self.model.objects.filter(query)

    def _get_query(self):
        title = self.request.GET.get('title')
        query = Q(title__icontains=title)
        district_pks = self.request.GET.getlist('districts')
        if district_pks:
            query &= Q(district__pk__in=district_pks)
        return query


class SchoolInfoAndResultsView(TemplateView):
    template_name = 'school_info_popup_content.html'

    def get_context_data(self, **kwargs):
        context = super(SchoolInfoAndResultsView, self).get_context_data(**kwargs)
        school_id = kwargs.pop('school_id')
        school = School.objects.get(pk=school_id)

        calculator = AverageResultsCalculator(school)
        result = calculator.calculate()
        context['school'] = school
        context['students_count'] = NTC.objects.filter(school=school).count()
        context['school_averages'] = result.get_school_averages()
        context['country_averages'] = result.get_country_averages()
        context['subjects'] = json.dumps(result.get_subjects())
        return context
