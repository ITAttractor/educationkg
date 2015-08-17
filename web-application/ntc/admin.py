from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from ntc.models import ParsedNTC, IntegrationQueue, NTC


class IntegratedListFilter(SimpleListFilter):
    title = "Integration status"

    parameter_name = 'integrated'

    def lookups(self, request, model_admin):
        return (
            ("True", "Integrated"),
            ("False", "Not integrated"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'True':
            return queryset.filter(ntc__isnull=False)
        elif value == 'False':
            return queryset.filter(ntc__isnull=True)
        else:
            return queryset


class ParsedNTCAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'location', 'school_title', 'timestamp', 'integrated', 'queue']
    search_fields = ['full_name', 'location', 'school_title', 'timestamp']
    list_filter = [IntegratedListFilter, 'location', 'school_title', 'integration_queue']

    def integrated(self, obj):
        try:
            obj.ntc
            return True
        except ObjectDoesNotExist:
            return False

    integrated.boolean = True

    def queue(self, obj):
        return '<a href="{url}?q={query}">Queue({query})</a>'.format(url=reverse('admin:ntc_integrationqueue_changelist'), query=obj.integration_queue.id)

    queue.allow_tags = True


class IntegrationQueueAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'status', 'parsed_ntc_count', 'not_integrated_count', 'show_not_integrated_items', 'integrate']
    search_fields = ['id']
    list_filter = ['status']

    def parsed_ntc_count(self, obj):
        return obj.parsedntc_set.count()

    def not_integrated_count(self, obj):
        return obj.parsedntc_set.filter(ntc__isnull=True).count()

    def show_not_integrated_items(self, obj):
        return '<a href="{url}?integrated=False&integration_queue__id__exact={id}">{count} items</a>'.format(url=reverse('admin:ntc_parsedntc_changelist'), id=obj.id,
                                                                                                             count=self.not_integrated_count(obj))

    def integrate(self, obj):
        html = '''<a class='button' href='%s'>Integrate</a>'''
        url = reverse("integrate_ntc", kwargs={"queue_id": obj.id})
        return html % url

    show_not_integrated_items.allow_tags = True
    integrate.allow_tags = True
    parsed_ntc_count.short_description = "Parsed"
    not_integrated_count.short_description = "Not integrated"


class NTCAdmin(admin.ModelAdmin):
    list_display = ["full_name", "school"]
    search_fields = ['full_name', 'school']


admin.site.register(NTC, NTCAdmin)
admin.site.register(IntegrationQueue, IntegrationQueueAdmin)
admin.site.register(ParsedNTC, ParsedNTCAdmin)
