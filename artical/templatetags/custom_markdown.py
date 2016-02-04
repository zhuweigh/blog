import markdown
from django.utils.safestring import mark_safe
from django import template
register = template.Library()
@register.filter(name='my_markdown')


def my_markdown(value):
	return mark_safe(markdown.markdown(value))
#def my_markdown(value):
#	return markdown.markdown(value)    
