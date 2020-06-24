from django import template

register = template.Library()


@register.filter
def loopnumequal(value, arg):
    if value in range(arg, 100, arg):
        return True


@register.filter
def loopnumequal_1(value, arg):
    if value in range(arg+1, 100, arg):
        return True
