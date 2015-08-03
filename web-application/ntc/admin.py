from django.contrib import admin
from ntc.models import ParsedNTC


class ParsedNTCAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'location', 'school_title', 'timestamp']
    search_fields = ['full_name', 'location', 'school_title', 'timestamp']
    list_filter = ['location', 'school_title']


admin.site.register(ParsedNTC, ParsedNTCAdmin)