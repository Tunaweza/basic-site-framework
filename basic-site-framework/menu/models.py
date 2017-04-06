from django.db import models

# Create your models here.
from ordered_model.models import OrderedModel


class Menu(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False, help_text='This is an internal title to help identify the menu.')
    slug = models.CharField(max_length=255, null=False, blank=False, help_text='This is an internal refernce to select the menu.')

    def __str__(self):
        return '%s' % self.title


class MenuItemManager(models.Manager):

    def get_queryset(self):
        qs = super(MenuItemManager, self).get_queryset()
        qs = qs.order_by('menu', 'order')
        return qs

class MenuItem(OrderedModel):

    menu = models.ForeignKey('menu.Menu', null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False, help_text='This is the visible title for the menu item.')
    link = models.CharField(max_length=255, null=False, blank=False, help_text='This is the link for the menu item.')
    public = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    logged_in = models.BooleanField(default=False)
    not_logged_in = models.BooleanField(default=False)

    order_with_respect_to = 'menu'


    def __str__(self):
        return '%s - %s' % (self.menu, self.title)
