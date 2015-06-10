# coding=utf-8
__author__ = 'had'

# The MIT License (MIT)
# Copyright (c) [2015] [Houtmann Hadrien]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('ticket.views',

                       url(r'^$', 'home.home'),
                       url(r'^login/$', 'auth.user_login'),
                       url(r'^add_ticket/$', 'tickets.add_ticket'),
                       url(r'^ticket_list_new/$', 'tickets.ticket_list_new'),
                       url(r'^ticket_list_clos/$', 'tickets.ticket_list_clos'),
                       url(r'^ticket_list_work/$', 'tickets.ticket_list_work'),
                       url(r'^ticket_list_incomplete/$', 'tickets.ticket_list_incomplet'),
                       url(r'^ticket_list_resolved/$', 'tickets.ticket_list_resolved'),
                       url(r'^ticket/edit_id=(?P<id>\d+)$', 'tickets.ticket_edit'),
                       url(r'^ticket/id=(?P<id>\d+)$', 'tickets.view_ticket', name='view'),
                       url(r'^ticket_all/$', 'tickets.ticket_all'),
                       url(r'^my_ticket_assign/$', 'tickets.my_ticket_assign'),
                       url(r'^delete/id=(?P<id>\d+)$', 'tickets.delete_ticket'),
                       url(r'^set_incomplete/id=(?P<id>\d+)$', 'tickets.set_incomplete'),
                       url(r'^set_complete/id=(?P<id>\d+)$', 'tickets.set_complete'),
                       url(r'^statistiques/$', 'stats.statistic'),
                       url(r'^ticket_stats/id=(?P<id>\d+)$', 'stats.ticket_stats', name='view'),
                       url(r'^logout/$', 'auth.logout_view'),



                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
