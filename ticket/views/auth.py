# coding=utf-8
__author__ = 'had'

# The MIT License (MIT)
# Copyright (c) [2015] [Houtmann Hadrien]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
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
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from ticket.forms.forms import ConnexionForm
from ticket.models import Tickets, UserProfile



def user_login(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                 """ Bloc pour prendre la config utilisateur, ou mettre par defaut
                 la valeur perpage, qui represente le nombre de ticket
                 afficher dans un tableau """
                try:
                    request.session['perpage'] = UserProfile.objects\
                                                .get(pk=request.user.pk).ticket_per_page
                except:
                    request.session['perpage'] = 25
                return redirect('/')

        else:
            pass

    else:
        pass

    form = ConnexionForm()
    return render_to_response('login.html', locals(), RequestContext(request))


@login_required(login_url='login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
