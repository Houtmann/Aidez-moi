__author__ = 'had'

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ticket.models import Tickets, UserProfile, Follow
from ticket.views.auth import home

from django.http import HttpResponse


@login_required(login_url='login/')
def telecharger_fichier(request, id):
    # Faire un truc ici qui génère le fichier
    # ou qui récupère un fichier existant.
    # l'important est d'avoir le chemin ABSOLU du fichier
    chemin_vers_fichier = Tickets.objects.get(id).filter('file')

    # On crée la réponse à la main
    response = HttpResponse()

    # On laisse nginx s'occuper de détecter le mimetype
    del response['content-type']
    # On met un header que nginx va comprendre comme "sert le fichier à ma place"
    response['X-Accel-Redirect'] = chemin_vers_fichier
    return response