from django import template
from django.db.models.query_utils import Q

from menu.models import MenuItem

register = template.Library()

#
# def get_menu(request):
#     active_link = request.path
#     menu_items = MenuItem.objects.all()
#     for item in menu_items:
#         if item.link == active_link:
#             item.active = True
#
#     return {'menu_items': menu_items}
#

@register.simple_tag(takes_context=True)
def get_menu(context, menu_name):
    if 'parent_path' in context:
        active_link = context['parent_path']
    else:
        active_link = context['request'].path

    is_admin = context['request'].user.is_superuser
    is_logged_in = context['request'].user.is_anonymous
    if is_admin:
        q = Q(
            Q(menu__slug=menu_name) & Q(admin=True) | Q(admin=False)
        )

    else:
        q = Q(
            Q(menu__slug=menu_name) and Q(admin=False)
        )


    menu_items = MenuItem.objects.filter(q)
    for item in menu_items:
        if item.link == active_link:
            item.active = True
    return menu_items

@register.simple_tag()
def get_active_menu_item(menu_items):
    for item in menu_items:
        if hasattr(item, 'active'):
            return item

    return None
