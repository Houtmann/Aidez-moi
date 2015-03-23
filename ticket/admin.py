
# Register your models here.
from django.contrib import admin
from .models import *



def close(modeladmin, request, queryset):
    queryset.update(status='4')
close.short_description = " Clore les tickets selectionnés"


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'created', 'status', 'priority' )
    actions = [close]




admin.site.register(Tickets, TicketsAdmin)
# Register your models here.