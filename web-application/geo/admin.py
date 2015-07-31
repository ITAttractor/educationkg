from django.contrib import admin
from geo.models import Region, District


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['title', 'region']


admin.site.register(Region)
admin.site.register(District, DistrictAdmin)
