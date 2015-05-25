__author__ = 'had'

from ticket.models import Tickets, UserProfile, Follow
import json


def compare(dict1, dict2):
    """

    :param dict1: Un dictionnaire
    :param dict2: Un autre dictionnaire
    :return:
    Compare deux dictionnaires afin de crée un suivi du ticket

    """
    sharedKeys = set(dict1.keys()).intersection(dict2.keys())
    for key in sharedKeys:
        if dict1[key] != dict2[key]:

            t1=dict(Tickets._meta.get_field_by_name(key)[0].flatchoices).get(dict1[key])
            t2=dict(Tickets._meta.get_field_by_name(key)[0].flatchoices).get(dict2[key])
            return('{} changé de {} à {}'.format(
                        Tickets._meta.get_field_by_name(key)[0].verbose_name,
                        t1, t2))