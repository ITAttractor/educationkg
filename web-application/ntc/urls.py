from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from ntc.views import NTCDataLoadApiView, IntegrateView, IndexView

urlpatterns = [
    url("^$", IndexView.as_view(), name='homepage'),
    url(r'^api/ntc/$', csrf_exempt(NTCDataLoadApiView.as_view())),
    url(r'^integrate/(?P<queue_id>\d+)/$', IntegrateView.as_view(), name='integrate_ntc')
]
