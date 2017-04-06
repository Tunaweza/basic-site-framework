from django import template
from django.db.models.query_utils import Q

from snippets.models import Snippet

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

@register.simple_tag()
def get_snippets(menu_item, placement):
    snippets = Snippet.objects.filter(placement=placement, menu_item=menu_item)
    return snippets
