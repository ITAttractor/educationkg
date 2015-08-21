import json
from django.db.models import Avg
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import View, TemplateView
from django.conf import settings

from geo.models import Region, District
from ntc.data_integrator import DataIntegrator
from ntc.data_saver import NTCDataSaver
from ntc.models import IntegrationQueue, NTC
from schools.models import School

SUBJECTS_DICT = {
    'math': _("Math"),
    'physics': _("Physics"),
    'chemistry': _("Chemistry"),
    'geometry': _("Geometry"),
    'biology': _("Biology"),
    'geography': _("Geography"),
    'history': _("History"),
    'eng_lang': _("English language"),
    'ger_lang': _("German language"),
    'fr_lang': _("French language"),
    'kyr_lang': _("Kyrgyz language"),
    'rus_lang': _("Russian language"),
    'uzb_lang': _("Uzbek language"),
    'informatics': _("Informatics"),
    'civics': _("Civics")
}


class NTCDataLoadApiView(View):
    def post(self, request, *args, **kwargs):
        if request.META.get('AUTHORIZATION') == settings.API_KEY or request.META.get(
                'HTTP_AUTHORIZATION') == settings.API_KEY:
            data_saver = NTCDataSaver(request.body)
            data_saver.load()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'error': 'wrong api key'}, status=401)


class IntegrateView(View):
    def get(self, request, *args, **kwargs):
        integration_queue = IntegrationQueue.objects.get(pk=kwargs['queue_id'])
        integrator = DataIntegrator(integration_queue)
        integrator.integrate()

        return redirect(request.META['HTTP_REFERER'])


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['total_schools'] = School.objects.count()
        context['total_students'] = NTC.objects.count()
        context['regions'] = Region.objects.all()
        bishkek = Region.objects.get(slug='city_bishkek')
        context['default_districts'] = District.objects.filter(region=bishkek)
        context['subjects'] = SUBJECTS_DICT
        return context


class TopSchoolBySubjectAndDistrictView(TemplateView):
    template_name = 'top_schools.html'

    def get_context_data(self, **kwargs):
        context = super(TopSchoolBySubjectAndDistrictView, self).get_context_data(**kwargs)
        district_id = self.request.GET.get("district_id")
        subject_key = self.request.GET.get("subject_key")

        schools = School.objects.filter(district__id=district_id)

        query_field_name = "ntc__%s" % subject_key
        context['schools'] = schools.values('title', 'id').annotate(avg=Avg(query_field_name)).order_by('-avg').exclude(avg=None)[:10]
        return context


class SearchResultView(TemplateView):
    template_name = 'result_list.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        full_name = kwargs.pop("full_name")
        if full_name:
            context['ntc_objects'] = NTC.objects.filter(full_name__istartswith=full_name)
        return context


class GetResultView(TemplateView):
    template_name = 'result_popup_content.html'

    def get_context_data(self, **kwargs):
        context = super(GetResultView, self).get_context_data(**kwargs)
        result_id = kwargs.pop('result_id')
        context['result'] = NTC.objects.get(pk=result_id)
        return context
