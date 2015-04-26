__author__ = 'had'

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django_tables2 import RequestConfig
from django.contrib import messages
from ticket.forms import ConnexionForm
from ticket.models import Tickets
from ticket.tables import TicketsTables


@login_required(login_url='login/')
def home(request):

    if request.user.is_staff:
        ticket_list = Tickets.objects.select_related('create_by', 'assign_to', 'category'
                                              ).filter(assign_to=request.user).order_by('-created')[:10:1]

        ticket_incomplete = Tickets.objects.filter(incomplete=0).count()
    else:
        ticket_list = Tickets.objects.filter(
                                create_by=request.user).order_by('-created')[:10:1]

        ticket_incomplete = Tickets.objects.filter(
                                create_by=request.user,
                                incomplete=0).count()

    if ticket_incomplete != 0:
        messages.add_message(request, messages.INFO,
                             "Vous avez %s tickets en attente d'informations complémenataires"
                             % (ticket_incomplete))
    else:
        pass

    return render(request, 'home.html', {'ticket_list': ticket_list})


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
