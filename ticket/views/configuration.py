# coding=utf-8

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


from django.shortcuts import render, redirect, get_object_or_404
from ticket.views.home import home
from ticket.forms.configuration_forms import ConfigForm
from ticket.models import User, UserProfile
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def view_configuration(request):
    """
    :param request:
    :return: La page qui sert de configuration pour les profiles utilisateurs
    """

    try:
        user = UserProfile.objects.get(user=request.user)
        config_form = ConfigForm(instance=user)

    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=request.user,
                                   active_mail=1,
                                   ticket_per_page=25)
        user = UserProfile.objects.get(user=request.user)


    if request.method == 'POST':

        config_form = ConfigForm(request.POST, instance=user)
        if config_form.is_valid():
            config = config_form.save()

            # met le cookies 'perpage' à jour avec la valeur ticket_per_page
            request.session['perpage'] = config.ticket_per_page
    else:
        config_form = ConfigForm(instance=user)

    return render(request, 'configuration.html', locals())