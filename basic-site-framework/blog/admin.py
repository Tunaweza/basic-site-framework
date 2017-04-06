from django.contrib import admin

# Register your models here.
from blog.models import BlogItem

admin.site.register(BlogItem)