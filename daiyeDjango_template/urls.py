"""daiyeDjango_template URL Configuration

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
from mytpl import views as v

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^one/', v.one),
    url(r'^two/', v.two),
    url(r'^three/', v.three),
    url(r'^four/', v.four),
    url(r'^five_get/', v.five_get),
    url(r'^five_post/', v.five_post),
]
