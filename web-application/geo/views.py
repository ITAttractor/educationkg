import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from geo.models import Region
from schools.models import School


class SchoolDataView(View):
    def get(self, request, *args, **kwargs):
        regions = Region.objects.all()
        data = {}
        data['total_schools'] = School.objects.count()
        for region in regions:
            districts = region.district_set.all()
            region_school_count = School.objects.filter(district__in=districts).count()
            region_data = {"school_count": region_school_count}
            region_data['title'] = region.title
            data[region.slug] = region_data
        return JsonResponse(data)


