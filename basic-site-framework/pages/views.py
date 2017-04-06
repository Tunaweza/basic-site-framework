from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from pages.models import Page


class PageView(TemplateView):
    queryset = Page.objects.all()
    template_name = 'pages/page.html'
    slug = ''

    def dispatch(self, request, *args, **kwargs):
        if 'slug' in kwargs:
            self.slug = kwargs['slug']
        return super(PageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        if self.slug != '':
            page = Page.objects.get(slug=self.slug)

        context['page'] = page

        return context
