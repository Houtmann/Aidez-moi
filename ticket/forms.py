__author__ = 'had'

from django import forms
from ticket.models import User, Tickets, UserProfile, response


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
                                                            'type':"text",
                                                            'placeholder':"Password"}))


class TicketForm(forms.ModelForm):
    """
    Pour ajouter un ticket
    """

    title = forms.CharField(label='Titre',widget=forms.TextInput(attrs={'placeholder': 'Titre',
                                                                        'size':'110',
                                                                        }))

    content = forms.CharField(label='Ticket',widget=forms.Textarea(attrs={'placeholder': 'Contenu du ticket',
                                                                          'rows':'5',

                                                                          'class':'uk-width-1-1'}))

    priority = forms.ChoiceField(
        choices=Tickets.PRIORITY_CHOICES,
        required=True,
        initial='3',
        label=('Urgency'),
        help_text=('Please select a priority carefully.'),
         )

    # Pour choisir que les membres du staff
    assign_to = forms.ModelChoiceField(queryset=User.objects.all().filter(is_staff=1))

    class Meta:
        model = Tickets
        exclude = ('created', 'create_by')

    def __init__(self, *args, **kwargs):
        """
        Pour exlcure certains champs de la classe TicketForm
        afin d'afficher assign_to et status pour un membre du staff
        """
        user = kwargs.pop('user', None)
        super(TicketForm, self).__init__(*args, **kwargs)
        if user.is_staff is False:
            del self.fields['assign_to']
            del self.fields['status']



class ResponseForm(forms.ModelForm):
    response = forms.CharField(label='Ticket',widget=forms.Textarea(
        attrs={'placeholder': 'Réponse au ticket','rows':'4','class':'uk-width-1-1'}))

    class Meta:
        model = response
        exclude = ('date_response', 'response_by', 'ticket_id')
