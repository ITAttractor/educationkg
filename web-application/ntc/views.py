from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView
from django.conf import settings

from geo.models import Region
from ntc.data_integrator import DataIntegrator
from ntc.data_saver import NTCDataSaver
from ntc.models import IntegrationQueue, NTC


class NTCDataLoadApiView(View):
    def post(self, request, *args, **kwargs):
        if request.META.get('AUTHORIZATION') == settings.API_KEY or request.META.get('HTTP_AUTHORIZATION') == settings.API_KEY:
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
        context['regions'] = Region.objects.all()
        return context


class SearchResultView(TemplateView):
    template_name = 'result_list.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        full_name = kwargs.pop("full_name")
        context['ntc_objects'] = NTC.objects.filter(full_name__istartswith=full_name)
        return context


class GetResultView(TemplateView):
    template_name = 'result_popup_content.html'

    def get_context_data(self, **kwargs):
        context = super(GetResultView, self).get_context_data(**kwargs)
        result_id = kwargs.pop('result_id')
        context['result'] = NTC.objects.get(pk=result_id)
        return context
