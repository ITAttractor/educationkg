from django.conf.urls import url
from schools.views import SchoolSearchView, SchoolInfoAndResultsView

urlpatterns = [
    url('^search/$', SchoolSearchView.as_view(), name='search'),
    url('^get-info/(?P<school_id>\d+)$', SchoolInfoAndResultsView.as_view(), name='get-info')
]
