from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from ntc.views import NTCDataLoadApiView

urlpatterns = [
    url(r'^api/ntc/$', csrf_exempt(NTCDataLoadApiView.as_view())),
]
