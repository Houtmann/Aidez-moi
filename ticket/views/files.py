# coding=utf-8
__author__ = 'had'

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