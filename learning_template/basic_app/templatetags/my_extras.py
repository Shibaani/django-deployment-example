from django import template

register = template.Library()

@register.filter(name='cut')
def cut_value(value,arg):
    # Cuts all values in 'ags'
    return value.replace(arg,'')

# register.filter('cut',cut_value)
