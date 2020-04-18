"""
Case№10: The gas station
Developers: Zhambaeva D., Rashidova A., Ganbat S.
"""

from random import randint
from ru_local import *

def time_for_oil(volume):
    """Determining the time for gas station."""

    volume = int(volume)
    volume = volume // 10
    if volume % 10 > 5:
        volume += 1
    plus_time = randint(-1, 1)
    volume += plus_time
    if volume == 0:
        return 1
    return volume

def get_value():
    """Getting value from reading azs.txt"""

    with open('azs.txt', 'r') as f:
        text = f.readlines()
        text = [line.strip() for line in text]
        value = len(text)
    return value


def azs():
    '''Reading azs.txt'''

    azs_info = {}

    with open('azs.txt', 'r') as f:
        text = f.readlines()
        text = [line.strip() for line in text]

        for i in range(len(text)):
            a = {}
            line = text[i]
            line = line.split()
            [a['max']] = line[1]
            k = []
            for j in range(2, len(line)):
                h = line[j]
                k.append(h)
            a.update({'oil': k})
            azs_info[line[0]] = a
    return azs_info


def clients_readinig():
    '''Readind input.txt and analyzing'''

    clients_info = {}
    with open('input.txt', 'r') as f:
        text = f.readlines()
        text = [line.strip() for line in text]
        for i in range(len(text)):
            b = {}
            line = text[i]
            line = line.split()
            minutes = time(line[0])
            b['V'] = line[1]
            b['oil'] = line[2]
            minutes_to_stop = time_for_oil(line[1])
            b['time_to_stop'] = minutes_to_stop
            b['time_to_go'] = minutes + minutes_to_stop
            clients_info[minutes] = b
    return clients_info


def price_oil():
    '''Creating a dictionary with market prices
       for gasoline brands'''

    price_oil_list = dict()
    price_oil_list[AI_80] = 39
    price_oil_list[AI_92] = 43
    price_oil_list[AI_95] = 46
    price_oil_list[AI_98] = 51
    return price_oil_list
