__author__ = 'had'
from django import forms
from ticket.models import User, Tickets, UserProfile, Follow
from model_utils import FieldTracker


class ConnexionForm(forms.Form):
    """
    Pour la page de login
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,
                               widget=forms.TextInput(attrs={
                                                            'type':"text",
                                                            'placeholder':"Username"}))
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(attrs={
                                                            'type':"password",
                                                            'placeholder':"Password"}))

class TicketForm(forms.ModelForm):
    """
    Pour ajouter un ticket
    """
    title = forms.CharField(label='Titre',
                            widget=forms.TextInput
                            (attrs={'placeholder': 'Titre',
                                    'size':'110',
                                    }))
    content = forms.CharField(label='Ticket',
                              widget=forms.Textarea
                              (attrs={'placeholder': 'Contenu du ticket',
                                      'rows':'5',
                                      'class':'uk-width-1-1'}))

    priority = forms.ChoiceField(
        choices=Tickets.PRIORITY_CHOICES,
        required=True,
        initial='3',
        label=('Urgence'),
        help_text=('Please select a priority carefully.'),
         )
    # Pour choisir que les membres du staff
    assign_to = forms.ModelChoiceField(queryset=User.objects.all().filter(is_staff=1))

    class Meta:
        model = Tickets
        exclude = ('created', 'create_by')

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



    def edit(self,ticket_id, user, *args, **kwargs):
        """
        :param ticket_id: Clé du ticket
        :param user: id de la session user
        La fonction edit est pour l'édition d'un ticket et elle permet de sauvegarder les
        élements changant dans la table Follow afin d'avoir un suivi du ticket"""

        if  Tickets.objects.filter(id=ticket_id).exists():
            if self.has_changed():

                ticket = Tickets.objects.filter(pk=ticket_id)
                for field in self.changed_data:

                    oldvalue = ticket.values(field)
                    #column = Tickets._meta.get_field(field).verbose_name
                    Follow.objects.create(
                                    ticket_id=ticket_id,
                                    field=Tickets._meta.get_field_by_name(field)[0].verbose_name, # Pour avoir le nom verbeux dans la table de suivi
                                    old_value=oldvalue[0].get(field),
                                    new_value=self[field].value(),
                                    follow_by=user
                                     )
        else:
            pass
        super(TicketForm, self).save(*args, **kwargs)


class ResponseForm(forms.ModelForm):
    follow = forms.CharField(label='Ticket',widget=forms.Textarea(
        attrs={'placeholder': 'Réponse au ticket','rows':'4','class':'uk-width-1-1'}))

    class Meta:
        model = Follow
        fields = ['follow']
        exclude = ('date_follow', 'ticket_id', 'field', 'new_value', 'old_value', 'follower')
