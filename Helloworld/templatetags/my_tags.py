from django import template

register = template.Library() #register的名字是固定的,不可改变
@register.filter
def my_filter(v1, v2):
    return v1 * v2