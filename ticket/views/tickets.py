__author__ = 'had'

from django.shortcuts import render, redirect, render_to_response
from ticket.forms import TicketForm, ResponseForm
from ticket.models import Tickets, UserProfile, Follow
from ticket.views.auth import home
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, Context, RequestContext
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from datetime import datetime

from tables import TicketsTables



PER_PAGE = 100

@cache_page(60*1)
@login_required(login_url='login/')
def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST, user=request.user)
        # return redirect('/')
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.create_by = request.user
            ticket.created = datetime.now()
            ticket.save()
            return redirect(home)
        else:
            return render(request, 'add_ticket.html', locals())
    else:
        form = TicketForm(user=request.user)
    return render(request, 'add_ticket.html', locals())


#@cache_page(60*1)
@login_required(login_url='login/')
def ticket_list_new(request):
    if request.user.is_staff:
        list = Tickets.objects.filter(assign_to=None).order_by('-created')
        ticket_list = TicketsTables(list)
    else:
        list = Tickets.objects.filter(create_by=request.user, assign_to=None).order_by('-created')
        ticket_list = TicketsTables(list)



    return render(request, 'ticket_list.html', locals())

#@cache_page(60*1)
@login_required(login_url='login/')
def ticket_list_work(request):

    if request.user.is_staff:
        list = Tickets.objects.select_related('create_by', 'assign_to').prefetch_related('create_by')\
            .filter(status='OPEN').exclude(assign_to=None).order_by('-created')
        ticket_list = TicketsTables(list)
    else:
        list = Tickets.objects.select_related('create_by', 'assign_to').prefetch_related('create_by')\
            .filter(create_by=request.user, status='OPEN').exclude(assign_to=None).order_by('-created')
        ticket_list = TicketsTables(list)

    return render(request, 'ticket_list.html', locals())


#@cache_page(60*1)
@login_required(login_url='login/')
def ticket_list_resolved(request):
    if request.user.is_staff:
        list = Tickets.objects.select_related('create_by', 'assign_to')\
            .filter(status='RESOLVED').exclude(assign_to=None).order_by('-created')
        ticket_list = TicketsTables(list)
    else:
        list = Tickets.objects.select_related('create_by', 'assign_to').prefetch_related('create_by')\
            .filter(create_by=request.user, status='RESOLVED').order_by('-created')
        ticket_list = TicketsTables(list)
    return render(request, 'ticket_list.html', locals())

#@cache_page(60*1)
@login_required(login_url='login/')
def ticket_list_clos(request):
    if request.user.is_staff:
        list = Tickets.objects.select_related('create_by', 'assign_to').prefetch_related('create_by', 'assign_to')\
            .filter(status='CLOSED').exclude(assign_to=None).order_by('-created')
        ticket_list = TicketsTables(list)
    else:
        list = Tickets.objects.select_related('create_by', 'assign_to').prefetch_related('create_by')\
            .filter(create_by=request.user, status='CLOSED').order_by('-created')
        ticket_list = TicketsTables(list)


    return render(request, 'ticket_list.html', locals())





@login_required(login_url='login/')
def ticket_all(request):
    list = Tickets.objects.select_related('create_by', 'assign_to')
    ticket_list = TicketsTables(list)

    return render(request, 'ticket_list.html', locals())



#@cache_page(60*15)
@login_required(login_url='login/')
def ticket_edit(request, id):
    ticket = get_object_or_404(Tickets, id=id)
    if request.method=='POST' and 'edit' in request.POST:
        form = TicketForm(request.POST, user=request.user, instance=ticket)

        if form.is_valid():
            #form.edit(commit=False, ticket_id=id, user=request.user)
            form.edit(ticket_id=id, user=request.user)
            #messages.add_message(request, messages.INFO, 'Ticket mis à jour OK')
            return redirect(view_ticket, id)
            # If the save was successful, redirect to another page
    else:
            form = TicketForm(user=request.user, instance=ticket)
            response = ResponseForm()

    return render(request, 'add_ticket.html', locals())





@login_required(login_url='login/')
def view_ticket(request, id):

    tickets = Tickets.objects.select_related('create_by').get(id=id)
    follow_up = Follow.objects.select_related('follow_by', 'ticket').filter(ticket=id)

    if request.method == 'POST':
        form = ResponseForm(data=request.POST)
        #if form.is_valid():
        follow = form.save(commit=False)
        follow.ticket_id=id
        follow.follow_by=request.user
        follow.save()
    else:
        form = ResponseForm()

    return render(request,'ticket.html', locals())




