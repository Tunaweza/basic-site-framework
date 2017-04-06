from django.db import models

# Create your models here.

class BlogItem(models.Model):

    title = models.CharField(help_text='The broswer title of the blog post.', blank=False, null=False, max_length=255)
    slug = models.CharField(help_text='The path of the blog post.', null=False, blank=False, max_length=255)
    meta_author = models.TextField(help_text='The author meta tag contents, if blank tag will not display.', null=True, blank=True)
    meta_description = models.TextField(help_text='The description meta tag contents, if blank tag will not display.', null=True, blank=True)
    meta_keywords = models.TextField(help_text='The keywords meta tag contents, if blank tag will not display.', null=True, blank=True)
    content = models.TextField(help_text='The html content of the blog post.', null=False, blank=True, default='')

    def __str__(self):
        return self.title