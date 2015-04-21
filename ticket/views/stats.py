__author__ = 'had'
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def statistic(request):

    return render(request, 'statistics.html', locals())