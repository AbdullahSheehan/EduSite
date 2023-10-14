from django import template
register = template.Library()

@register.filter
def ellipsis(val):
    return val[:300]+"..."