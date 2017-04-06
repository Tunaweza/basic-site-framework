from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

# Register your models here.
from menu.models import Menu, MenuItem

admin.site.register(Menu)

class MenuItemAdmin(OrderedModelAdmin):
    list_display = ('title', 'menu', 'link', 'order', 'move_up_down_links')

admin.site.register(MenuItem, MenuItemAdmin)
