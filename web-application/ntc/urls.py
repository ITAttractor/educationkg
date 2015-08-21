from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from ntc.views import NTCDataLoadApiView, IntegrateView, IndexView, SearchResultView, GetResultView, \
    TopSchoolBySubjectAndDistrictView

urlpatterns = [
    url("^$", IndexView.as_view(), name='homepage'),
    url("^search-result/(?P<full_name>.*)/$", SearchResultView.as_view(), name='search_result'),
    url("^get-top/$", TopSchoolBySubjectAndDistrictView.as_view(), name='top_schools'),
    url("^get-result/(?P<result_id>\d+)/$", GetResultView.as_view(), name='get_result'),
    url(r'^api/ntc/$', csrf_exempt(NTCDataLoadApiView.as_view())),
    url(r'^integrate/(?P<queue_id>\d+)/$', IntegrateView.as_view(), name='integrate_ntc'),
]
