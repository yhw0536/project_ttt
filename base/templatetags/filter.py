import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def mark(content):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(content, extensions=extensions))