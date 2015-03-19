__author__ = 'had'

from django.shortcuts import render, redirect, render_to_response
from ticket.forms import TicketForm, ResponseForm
from ticket.models import Tickets, UserProfile
from ticket.views.auth import home
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, Context, RequestContext
from django.contrib import messages


@login_required(login_url='login/')
def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST, user=request.user)
        # return redirect('/')
        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.create_by = request.user
            ticket.save()
            return redirect(home)
        else:
            return render(request, 'add_ticket.html', locals())
    else:
        form = TicketForm(user=request.user)
    return render(request, 'add_ticket.html', locals())


@login_required(login_url='login/')
def ticket_list_new(request):
    if request.user.is_staff:
        ticket = Tickets.objects.filter(assign_to=None).order_by('-created')
    else:
        ticket = Tickets.objects.filter(create_by=request.user, assign_to=None).order_by('-created')
    return render(request, 'ticket_list.html', locals())


@login_required(login_url='login/')
def ticket_list_work(request):
    if request.user.is_staff:
        ticket = Tickets.objects.select_related('username').exclude(assign_to=None).order_by('-created')
    else:
        ticket = Tickets.objects.filter(create_by=request.user, status=1).exclude(assign_to=None).order_by('-created')

    #return render_to_response('ticket_list.html',
        #RequestContext(request, {
            #'ticket': ticket,}))

    return render(request, 'ticket_list.html', locals())


@login_required(login_url='login/')
def ticket_list_resolved(request):
    if request.user.is_staff:
        ticket = Tickets.objects.filter(status=3).exclude(assign_to=None).order_by('-created')
    else:
        ticket = Tickets.objects.filter(create_by=request.user, status=3).order_by('-created')
    return render(request, 'ticket_list.html', locals())

@login_required(login_url='login/')
def ticket_list_clos(request):
    if request.user.is_staff:
        ticket = Tickets.objects.filter(status=4).exclude(assign_to=None).order_by('-created')
    else:
        ticket = Tickets.objects.filter(create_by=request.user, status=4).order_by('-created')
    return render(request, 'ticket_list.html', locals())


@login_required(login_url='login/')
def ticket_all(request):
    ticket = Tickets.objects.all
    return render(request, 'ticket_list.html', locals())


@login_required(login_url='login/')
def ticket_edit(request, id):

    ticket = get_object_or_404(Tickets, id=id)

    if request.method=='POST' and 'edit' in request.POST:
        form = TicketForm(request.POST, user=request.user, instance=ticket)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Ticket mis à jour OK')
            return redirect(ticket_edit, id)
            # If the save was successful, redirect to another page
    else:
            response = ResponseForm()
            form = TicketForm(user=request.user, instance=ticket)
    return render(request, 'add_ticket.html', locals())


def view_ticket(request, id):
    tickets = Tickets.objects.select_related('create_by').get(id=id)
    return render(request,'ticket.html', locals())




