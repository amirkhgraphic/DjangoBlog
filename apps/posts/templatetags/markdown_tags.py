import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def markdown_convertor(value: str) -> str:
    return markdown.markdown(value.strip(), extensions=['fenced_code'])
