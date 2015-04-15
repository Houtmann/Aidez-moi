
from django.contrib import admin
from .models import *
from django import forms


def close(modeladmin, request, queryset):
    queryset.update(status='4')
close.short_description = " Clore les tickets selectionnés"


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'created', 'status', 'priority' )
    actions = [close]


class TicketsCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tickets, TicketsAdmin)
admin.site.register(TicketCategory, TicketsCategoryAdmin)
