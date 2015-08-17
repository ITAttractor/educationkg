from django.db.models import Q
from django.views.generic import ListView
from schools.models import School


class SchoolSearchView(ListView):
    template_name = 'schools/partial_list_on_main_page.html'
    model = School
    paginate_by = 10
    context_object_name = 'schools'

    def get_queryset(self):
        query = self._get_query()
        return self.model.objects.filter(query)

    def _get_query(self):
        title = self.request.GET.get('title')
        query = Q(title__icontains=title)
        print self.request.GET
        district_pks = self.request.GET.getlist('districts')
        if district_pks:
            query &= Q(district__pk__in=district_pks)
        return query
