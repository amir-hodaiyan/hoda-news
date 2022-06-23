from django import template

register = template.Library()


@register.simple_tag
def trans_page(request, prefix_language):
    current_path = request.get_full_path()[4:]
    domain = request.META['HTTP_HOST']
    full_path = f"http://{domain}/{prefix_language}/{current_path}"
    return full_path
