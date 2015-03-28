__author__ = 'had'


from django.shortcuts import render, redirect, render_to_response
from ticket.forms import TicketForm, ConnexionForm
from ticket.models import Tickets

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseForbidden, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


# Create your views here.
@login_required(login_url='login/')
def home(request):
    if request.user.is_staff:
        ticket = Tickets.objects.filter(assign_to = request.user).order_by('-created')[:10:1]
    else:
        ticket = Tickets.objects.filter(create_by = request.user).order_by('-created')[:10:1]

    return render(request, 'home.html', locals())



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