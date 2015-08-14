from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView
from ntc.data_integrator import DataIntegrator
from ntc.data_saver import NTCDataSaver
from django.conf import settings
from ntc.models import IntegrationQueue


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
        return context

