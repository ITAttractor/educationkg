from django.conf.urls import url
from geo.views import SchoolDataView

urlpatterns = [
    url("^get-school-data/$", SchoolDataView.as_view(), name='school-data'),
]