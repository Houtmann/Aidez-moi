# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'Aidez-Moi Administration'  # Change le nom de l'administration

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'djangoticket.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^', include('ticket.urls')),


                       )
