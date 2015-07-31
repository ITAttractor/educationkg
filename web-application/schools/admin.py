from django.contrib import admin
from schools.models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'phone', 'district']


admin.site.register(School, SchoolAdmin)