from django import template

register = template.Library()


@register.inclusion_tag('schools/pagination.html', takes_context=True)
def paginate(context, url):
    get_params = context['request'].GET.copy()
    if 'page' in get_params:
        del get_params['page']
    if len(get_params.keys()) > 0:
        get_params = "&%s" % get_params.urlencode()
    else:
        get_params = ''
    return {
        'is_paginated': context['is_paginated'],
        'page_obj': context['page_obj'],
        'paginator': context['paginator'],
        'object_list': context['object_list'],
        'url': url,
        'get_params': get_params,
    }
