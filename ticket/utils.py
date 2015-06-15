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


from ticket.models import Tickets, UserProfile, Follow
import json


def compare_two_dict(dict_one, dict_two):
    """
    :param dict_one: Un dictionnaire
    :param dict_two: Un autre dictionnaire
    :return:
    Retourne les différences entre old_value et new_value dans la table de suivi Follow
    pour l'afficher dans la timeline de suivi de la page d'un ticket
    Compare deux dictionnaires afin de crée un suivi du ticket
    """

    dict1 = json.loads(dict_one)
    dict2 = json.loads(dict_two)
    sharedkeys = set(dict1.keys()).intersection(dict2.keys())

    for key in sharedkeys:
        t1 = dict(Tickets._meta.get_field_by_name(key)[0].flatchoices).get(dict1[key])
        t2 = dict(Tickets._meta.get_field_by_name(key)[0].flatchoices).get(dict2[key])
        if t1 and t2 != None:
            yield Tickets._meta.get_field_by_name(key)[0].verbose_name \
              + _(' changé de ') \
              + t1 \
              + _(' à ') \
              + t2
