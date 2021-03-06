"""webapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ntc.urls', namespace='ntc')),
    url(r'^school/', include('schools.urls', namespace='schools')),
    url(r'geo/', include('geo.urls', namespace='geo')),
    url(r'pages/', include('django.contrib.flatpages.urls')),
    url('^favicon\.ico$', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'), permanent=False))
]
