from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.admin import AdminSite
from .models import *


def close(modeladmin, request, queryset):
    """Pour clore tous les tickets selectionnés"""
    queryset.update(status='4')
    close.short_description = " Clore les tickets selectionnés"





class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'created', 'status', 'priority')
    actions = [close]

admin.site.register(Tickets, TicketAdmin)


class TicketCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(TicketCategory, TicketCategoryAdmin)


class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'telephone', )
    pass
admin.site.register(Entity, EntityAdmin)


# Pour rajouter dans l'interface user dans l'admin la line Entity
class UserProfileInline(admin.TabularInline):
    model = UserProfile


class MyUserAdmin(UserAdmin):

    def entity(self, obj):
        """
        Retourne l'entité à laquelle appartient l'utilisateur
        """
        entity = obj.userprofile.entity
        return entity
    entity.short_description = _('Entité')

    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'date_joined', 'last_login', 'is_active', 'is_staff', 'entity', )

    list_select_related = True
    inlines = [
        UserProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
