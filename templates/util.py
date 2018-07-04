from django import template
from django.utils.safestring import mark_safe
from django.template import Library

import json

register = template.Library()

@register.filter
def get_type(value):
    return type(value).__name__


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))