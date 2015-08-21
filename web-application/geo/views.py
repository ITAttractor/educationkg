import json
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.translation import ungettext
from django.views.generic import View
from geo.models import Region, District
from ntc.models import NTC
from schools.models import School


class SchoolDataView(View):
    def get(self, request, *args, **kwargs):
        regions = Region.objects.all()
        data = {}
        data['total_schools'] = School.objects.count()
        for region in regions:
            districts = region.district_set.all()
            region_school_count = School.objects.filter(district__in=districts).count()
            region_data = {"school_count": region_school_count, 'title': region.title, 'case': region.prepositional_case, 'school_case': ungettext("school", "schools", region_school_count)}
            data[region.slug] = region_data
        return JsonResponse(data)


class DistrictsByRegionView(View):
    def get(self, request, *args, **kwargs):
        region_id = request.GET.get("region_id")
        districts = District.objects.filter(region__id=region_id).values("id", "title")
        response = json.dumps(list(districts))
        return HttpResponse(response, content_type="application/json")

