__author__ = 'had'
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from ticket.models import Tickets
from ticket.views.tickets import *

class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Tickets.objects.order_by('-created')[:20]

    def item_title(self, item):
        return item.title

    def item_date(self, item):
        return item.created

    def item_description(self, item):
        return item.content

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse(view_ticket, args=[item.pk])