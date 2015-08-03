from django.http.response import JsonResponse
from django.views.generic.base import View
from ntc.data_saver import NTCDataSaver
from django.conf import settings


class NTCDataLoadApiView(View):
    def post(self, request, *args, **kwargs):
        if request.META.get('AUTHORIZATION') == settings.API_KEY or request.META.get('HTTP_AUTHORIZATION') == settings.API_KEY:
            data_saver = NTCDataSaver(request.body)
            data_saver.load()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'error': 'wrong api key'}, status=401)

