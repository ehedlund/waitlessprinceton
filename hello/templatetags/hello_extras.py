from django import template

register = template.Library()

@register.filter
def getIndex(List, i):
    return List[int(i)]