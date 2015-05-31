# coding=utf-8
__author__ = 'had'

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from ticket.forms import ConnexionForm
from ticket.models import Tickets



def user_login(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
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
