
# Register your models here.
from django.contrib import admin
from .models import *
from django import forms
from simple_history.admin import SimpleHistoryAdmin


def close(modeladmin, request, queryset):
    queryset.update(status='4')
close.short_description = " Clore les tickets selectionnés"


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'created', 'status', 'priority' )
    actions = [close]

class TicketsAdminWithHistory(TicketsAdmin, SimpleHistoryAdmin):
    list_display = ('title', 'types', 'created', 'status', 'priority' )
    actions = [close]

admin.site.register(Tickets, TicketsAdminWithHistory)


