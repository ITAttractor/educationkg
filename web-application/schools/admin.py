from django.contrib import admin
from schools.models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'phone', 'region', 'district']
    list_filter = ['district__region', 'district']

    def region(self, obj):
        return obj.district.region


admin.site.register(School, SchoolAdmin)