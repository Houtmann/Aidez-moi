# coding=utf-8
__author__ = 'had'
from django import forms
from ticket.models import User, Tickets, UserProfile, Follow
from django.utils.translation import ugettext as _
from djangoticket.settings import USE_MAIL
from ticket.tasks import follow_on_ticket
from django.contrib import messages
import json


class ConnexionForm(forms.Form):
    """
    Pour la page de login
    """
    username = forms.CharField(label=_("Nom d'utilisateur"), max_length=30,
                               widget=forms.TextInput(attrs={
                                   'type': "text",
                                   'placeholder': "Username"}))

    password = forms.CharField(label=_("Mot de passe"),
                               widget=forms.PasswordInput(attrs={
                                   'type': "password",
                                   'placeholder': "Password"}))


class TicketForm(forms.ModelForm):
    """
    Pour ajouter un ticket
    """
    title = forms.CharField(label=_('Titre'),
                            widget=forms.TextInput
                            (attrs={'placeholder': _('Titre'),
                                    'size': '110',
                                    }))
    content = forms.CharField(label=_('Ticket'),
                              widget=forms.Textarea
                              (attrs={'placeholder': _('Contenu du ticket'),
                                      'rows': '5',
                                      'class': 'uk-width-1-1'}))

    priority = forms.ChoiceField(
        choices=Tickets.PRIORITY_CHOICES,
        required=True,
        initial='3',
        label=(_('Urgence')),
        help_text=(_('Veuillez selectionner une priorité.')),
    )

    # Pour choisir que les membres du staff
    assign_to = forms.ModelChoiceField(
                    queryset=User.objects.all().filter(is_staff=1),
                    label=_('Assigné à'),
                    required=False)
    file = forms.FileField(required=False)

    class Meta:
        model = Tickets
        exclude = ('created', 'create_by', 'complete')


    def __init__(self, *args, **kwargs):
        """
        Pour exclure certains champs de la classe TicketForm
        afin d'afficher assign_to et status pour un membre du staff
        """
        user = kwargs.pop('user', None)
        super(TicketForm, self).__init__(*args, **kwargs)
        if user.is_staff is False:
            del self.fields['assign_to']
            #del self.fields['status']



    def close(self, ticket_id, user):

        """ Fonction pour clore un ticket"""

        ticket = Tickets.objects.get(pk=ticket_id)
        if ticket.depends_on == '':
            self.edit(ticket_id, user)
        else:
            raise Exception(_('vous devez clore le ticket %s') % ticket.depends_on)



    def save_one(self, ticket_id, user, *args, **kwargs):
        """
        :param ticket_id: Clé du ticket
        :param user: id de la session user
        La fonction edit est pour l'édition d'un ticket et elle permet de sauvegarder les
        élements changant dans la table Follow afin d'avoir un suivi du ticket
        """
        old_value = {} # Dictionnaire pour envoyer les valeurs changées dans le worker celery
        new_value = {}
        if Tickets.objects.filter(id=ticket_id).exists():
            if self.has_changed():
                ticket = Tickets.objects.filter(pk=ticket_id)

                for field in self.changed_data:
                    new = self[field].value()
                    old_value[field] = ticket.values(field)[0].get(field)
                    new_value[field] = new

                Follow.objects.create(
                        ticket_id=ticket_id,
                        field='',
                        old_value=json.dumps(old_value),
                        new_value=json.dumps(new_value),
                        follow_by=user)

                if USE_MAIL:
                    follow_on_ticket.delay(ticket_id, old_value, new_value)


        else:
            pass
        super(TicketForm, self).save(*args, **kwargs)




class StatusForm(TicketForm, forms.ModelForm):
    """
    Pour modifier le statut du ticket
    """

    status = forms.CharField(required=False,
                             widget=forms.Select(
                             choices=Tickets.STATUS_CHOICES))

    class Meta:
        model = Tickets
        fields = ['status']
        exclude = ('title',
                   'content',
                   'created',
                   'priority',
                   'last_edited',
                   'complete',
                   'depends_on',
                   'types',
                   'assign_to',
                   'category',
                   'create_by',
                   'ask_to_delete',)

    def __init__(self, *args, **kwargs):
        """
        Pour exclure certains champs de la classe TicketForm
        afin d'afficher assign_to et status pour un membre du staff
        """
        super(StatusForm, self).__init__(*args, **kwargs)
        del self.fields['priority']
        del self.fields['title']
        del self.fields['content']



    def close(self, ticket_id, user):
        """ Fonction pour clore un ticket"""

        ticket = Tickets.objects.get(pk=ticket_id)
        if ticket.depends_on == '':

            self.edit(ticket_id, user)

        else:
            raise Exception(_('vous devez clore le ticket %s') % ticket.depends_on)


class ResponseForm(forms.ModelForm):
    follow = forms.CharField(label='Ticket', required=False, widget=forms.Textarea(
        attrs={'placeholder': _('Réponse au ticket'),
               'rows': '4',
               'class': 'uk-width-1-1'}))

    class Meta:
        model = Follow
        fields = ['follow']
        exclude = (
            'date_follow',
            'ticket_id',
            'field',
            'new_value',
            'old_value',
            'follower')
