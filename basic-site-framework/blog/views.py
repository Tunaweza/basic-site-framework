from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import BlogItem


class BlogListView(ListView):
    queryset = BlogItem.objects.all()
    template_name = 'blog/list.html'


class BlogDetailView(DetailView):
    queryset = BlogItem.objects.all()
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['parent_path'] = '/blog/'
        return context