__author__ = 'had'

from django.shortcuts import render, redirect, render_to_response
from ticket.forms import TicketForm, ConnexionForm
from ticket.models import Tickets
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from ticket.tables import TicketsTables
from django_tables2 import RequestConfig
from django.views.decorators.cache import cache_page

# Create your views here.
#@cache_page(60*3)
@login_required(login_url='login/')
def home(request):
    if request.user.is_staff:
        list = Tickets.objects.select_related('create_by', 'assign_to').filter(assign_to = request.user).order_by('-created')[:25:1]
        ticket_list = TicketsTables(list)
    else:
        list = Tickets.objects.filter(create_by = request.user).order_by('-created')[:25:1]
        ticket_list = TicketsTables(list)

    RequestConfig(request, paginate={"per_page": 25}).configure(ticket_list)
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