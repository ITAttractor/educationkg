from django.conf.urls import url
from schools.views import SchoolSearchView

urlpatterns = [
    url('^search/$', SchoolSearchView.as_view(), name='search'),
]
