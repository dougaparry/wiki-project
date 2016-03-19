"""wikiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
# Date 28th May
# Group: Charne, Cleo, Doug, Jess

from django.conf.urls import include, url
from django.contrib import admin
from wikiapp import views

# Dynamic Url regular expressions to match to corresponding views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wikijourney$', 'wikiapp.views.home_page'),
    url(r'^wikijourney/join/$', 'wikiapp.views.join_page'), 
    url(r'^wikijourney/guest/$', 'wikiapp.views.guest'),
    url(r'^wikijourney/loginpage/$', 'wikiapp.views.log_in_page'), 
    url(r'^wikijourney/userlogin/$', 'wikiapp.views.login'), 
    url(r'^wikijourney/userlogout/$', 'wikiapp.views.logout'), 
    url(r'^wikijourney/create/$', 'wikiapp.views.create_profile'),  
    url(r'^wikijourney/profile/$', 'wikiapp.views.user_profile'),
    url(r'^wikijourney/country/$', 'wikiapp.views.country_page'), 
    url(r'^wikijourney/help/$', 'wikiapp.views.help_page'), 
    url(r'^wikijourney/(?P<page_name>[^/]+)/edit/revert/(\d+)$', 'wikiapp.views.revert'),   
    url(r'^wikijourney/(?P<page_name>[^/]+)/save/$', 'wikiapp.views.save_article'),
    url(r'^wikijourney/(?P<page_name>[^/]+)/edit/$', 'wikiapp.views.edit_article'),
    url(r'^wikijourney/(?P<page_name>[^/]+)/$', 'wikiapp.views.view_article'),
]
