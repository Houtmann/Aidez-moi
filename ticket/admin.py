# coding=utf-8
# The MIT License (MIT)
# Copyright (c) [2015] [Houtmann Hadrien]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the Aidez-moi), to deal
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


from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.admin import AdminSite
from .models import *




def close(modeladmin, request, queryset):
    """Pour clore tous les tickets selectionnés"""
    queryset.update(status='4')
    close.short_description = " Clore les tickets selectionnés"


class FollowAdmin(admin.ModelAdmin):
    pass


admin.site.register(Follow, FollowAdmin)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'created', 'status', 'priority', 'file')
    actions = [close]


admin.site.register(Tickets, TicketAdmin)


class TicketCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(TicketCategory, TicketCategoryAdmin)


class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'telephone',)
    pass


admin.site.register(Entity, EntityAdmin)




