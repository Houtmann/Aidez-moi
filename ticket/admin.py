
# Register your models here.
from django.contrib import admin
from .models import *



class TicketsAdmin(admin.ModelAdmin):


   list_display   = ('title', )


admin.site.register(Tickets, TicketsAdmin)
# Register your models here.


