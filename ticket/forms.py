__author__ = 'had'
from django import forms
from ticket.models import User, Tickets, UserProfile, Follow
from django.utils.translation import ugettext as _
from django.contrib.admin.util import display_for_field


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
        label=_('Assigné à'))

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
            del self.fields['status']
            del self.fields['depends_on']



    def edit(self, ticket_id, user, *args, **kwargs):
        """
        :param ticket_id: Clé du ticket
        :param user: id de la session user
        La fonction edit est pour l'édition d'un ticket et elle permet de sauvegarder les
        élements changant dans la table Follow afin d'avoir un suivi du ticket

        """
        if Tickets.objects.filter(id=ticket_id).exists():
            if self.has_changed():
                ticket = Tickets.objects.filter(pk=ticket_id)

                for field in self.changed_data:
                    oldvalue = ticket.values(field)
                    new = self[field].value()
                    print(self.changed_data)
                    # column = Tickets._meta.get_field(field).verbose_name
                    Follow.objects.create(
                            ticket_id=ticket_id,
                            field=Tickets._meta.get_field_by_name( # Pour avoir le nom verbeux dans la table de suivi
                                            field)[0].verbose_name,

                            old_value=dict(Tickets._meta.get_field_by_name(field)[0].flatchoices)
                                                                            .get(oldvalue[0].get(field)),
                            new_value=dict(Tickets._meta.get_field_by_name(field)[0].flatchoices)[(new)],

                            follow_by=user)

        else:
            pass
        super(TicketForm, self).save(*args, **kwargs)




class StatusForm(forms.ModelForm):

    """
    Pour modifier le statut du ticket
    """

    status = forms.CharField(required=False,
                widget=forms.Select(choices=Tickets.STATUS_CHOICES))
    class Meta:
        model = Tickets
        fields = ['status']
        exclude = ('title',
                   'content',
                   'created',
                   'last_edited',
                   'complete',
                   'depends_on',
                   'types',
                   'assign_to',
                   'category',
                   'create_by',)


    def edit(self, ticket_id, user, *args, **kwargs):
        """
        :param ticket_id: Clé du ticket
        :param user: id de la session user
        La fonction edit est pour l'édition d'un ticket et elle permet de sauvegarder les
        élements changant dans la table Follow afin d'avoir un suivi du ticket

        """
        if Tickets.objects.filter(id=ticket_id).exists():
            if self.has_changed():
                ticket = Tickets.objects.filter(pk=ticket_id)

                for field in self.changed_data:
                    oldvalue = ticket.values(field)
                    new = self[field].value()
                    print(self.changed_data)
                    # column = Tickets._meta.get_field(field).verbose_name
                    Follow.objects.create(
                            ticket_id=ticket_id,
                            field=Tickets._meta.get_field_by_name( # Pour avoir le nom verbeux dans la table de suivi
                                            field)[0].verbose_name,

                            old_value=dict(Tickets._meta.get_field_by_name(field)[0].flatchoices)
                                                                            .get(oldvalue[0].get(field)),
                            new_value=dict(Tickets._meta.get_field_by_name(field)[0].flatchoices)[(new)],

                            follow_by=user)

        else:
            pass
        super(TicketForm, self).save(*args, **kwargs)




class ResponseForm(forms.ModelForm):

    follow = forms.CharField(label='Ticket', required=False, widget=forms.Textarea(
        attrs={'placeholder': _('Réponse au ticket'), 'rows': '4', 'class': 'uk-width-1-1'}))

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
