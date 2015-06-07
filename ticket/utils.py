__author__ = 'had'

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