from django import template

from menu.models import Item

register = template.Library()


@register.inclusion_tag('tags/draw_next.html', takes_context=True)
def draw_next(context, slug):
    try:
        item = Item.objects.prefetch_related('items__items__items').get(slug=slug)
        return {'item': item, 'context': context}
    except Item.DoesNotExist:
        return {'item': '', 'context': context}
