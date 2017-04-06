from django.db import models

# Create your models here.

class Snippet(models.Model):

    placement = models.CharField(max_length=255, null=False, blank=False)
    menu_item = models.ManyToManyField('menu.MenuItem')
    heading = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return '%s - %s' % (self.heading, self.placement)