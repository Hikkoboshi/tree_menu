from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('tags/draw_menu.html', takes_context=True)
def draw_menu(context, slug):
    try:
        menu = Menu.objects.prefetch_related('items__items__items').get(title=slug)
        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}
