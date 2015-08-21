from django.conf.urls import url
from geo.views import SchoolDataView, DistrictsByRegionView

urlpatterns = [
    url("^get-school-data/$", SchoolDataView.as_view(), name='school-data'),
    url("^get-districts/$", DistrictsByRegionView.as_view(), name='districts'),
]