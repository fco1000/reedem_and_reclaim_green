# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def subtract(value, arg):
    try:
        return float(value) - float(arg)
    except ValueError:
        return None