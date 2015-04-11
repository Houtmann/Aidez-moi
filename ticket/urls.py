__author__ = 'had'

from django.conf.urls import patterns, url
from ticket.views import tickets, auth

urlpatterns = patterns('ticket.views',

    url(r'^$', 'auth.home'),
    url(r'^login/$', 'auth.user_login'),
    url(r'^add_ticket/$', 'tickets.add_ticket'),
    url(r'^ticket_list_new/$', 'tickets.ticket_list_new'),
    url(r'^ticket_list_clos/$', 'tickets.ticket_list_clos'),
    url(r'^ticket_list_work/$', 'tickets.ticket_list_work'),
    url(r'^ticket_list_resolved/$', 'tickets.ticket_list_resolved'),
    url(r'^ticket/edit_id=(?P<id>\d+)$', 'tickets.ticket_edit'),
    url(r'^ticket/id=(?P<id>\d+)$', 'tickets.view_ticket', name='view'),
    url(r'^ticket_all/$', 'tickets.ticket_all'),

    url(r'^logout/$', 'auth.logout_view'),


)