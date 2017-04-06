"""basic-site-framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import url, static, include
from django.contrib import admin

from basic_site_framework.settings import DEBUG
from blog.views import BlogListView, BlogDetailView
from basic_site_framework import settings
from pages.views import PageView

urlpatterns = [
    url(r'^$', PageView.as_view(), name='menu', kwargs={'slug': 'home'}),
    url(r'^blog/$', BlogListView.as_view(), name='blog_list'),
    url(r'^blog/(?P<pk>[0-9]+)-(?P<slug>[\w-]+).html$', BlogDetailView.as_view(), name='blog_detail'),

    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[\w-]+)/$', PageView.as_view(), name='page'),
    url(r'^(?P<slug>[\w-]+).html$', PageView.as_view(), name='page_html'),
]

if DEBUG:
    urlpatterns = urlpatterns + [url(r'^__debug__/', include(debug_toolbar.urls)),]

# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)