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


def queue_column():
    '''Preparing the columns for customers'''

    num_queue = dict()
    gasoline_brands_list = [AI_80, AI_92, AI_95, AI_98]
    for brand in gasoline_brands_list:
        num_queue[brand] = 0
    return  num_queue


def time(hours):
    """Counting the number of minutes."""

    h, m = hours.split(':')
    minutes = int(h) * 60 + int(m)
    return minutes


def back_time(minutes):
    """Determining the time."""

    h = minutes // 60
    m = minutes - h * 60
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    phrase = str(h) + ':' + str(m)
    return phrase


def main():

    num_of_columns = get_value()
    evaluation_num = dict()
    evaluation_list = dict()
    queue_col = queue_column()
    azs_info = azs()
    price_oil_dict = price_oil()
    clients = clients_readinig()
    value = get_value()
    for n in range(1, num_of_columns + 1):
        evaluation_num[n] = 0
        evaluation_list[n] = []
    its_time_to_go = dict()
    queue = 0

    for i in range(1440):
        condition = 0
        if i in clients.keys():
            patrol = clients[i]['oil']
            mini = 1000
            for j in range(1, num_of_columns + 1):
                if patrol in azs_info[str(j)]['oil']:
                    if evaluation_num[j] < int(azs_info[str(j)]['max']):
                        if evaluation_num[j] < mini:
                            mini = evaluation_num[j]
                            evaluation_num[j] += 1

                            print(V, back_time(i), NEW_CLIENT, back_time(i),
                                  clients[i]['oil'], clients[i]['V'],
                                  clients[i]['time_to_stop'], QUEUE, j)

                            evaluation_list[j].append(i)
                            condition = 1
                            queue_col[clients[i]['oil']] += int(clients[i]['V'])
                            clients[i].update({'station': j})
                            counting_wait = 0
                            if len(evaluation_list[j]) == 1:
                                time1 = clients[evaluation_list[j][0]]['time_to_go']
                            if len(evaluation_list[j]) > 1:
                                time1 = clients[evaluation_list[j][0]]['time_to_go']
                                its_time_to_go[i] = time1
                                counting_wait = clients[evaluation_list[j][0]]['time_to_stop']
                                for f in range(1, len(evaluation_list[j])):
                                    r = evaluation_list[j][f]
                                    counting_wait += clients[r]['time_to_stop']
                                    time1 = evaluation_list[j][0] + counting_wait
                                    clients[evaluation_list[j][f]]['time_to_go'] = time1
                            its_time_to_go[i] = time1
                            break
            if condition == 0:
                print(V, back_time(i), NEW_CLIENT, back_time(i),
                      clients[i]['oil'], clients[i]['V'],
                      clients[i]['time_to_stop'], COULD_NOT_FILL_THE_CAR)
                queue += 1

            for k in range(1, value + 1):
                print(MACHINE_NUMBER, k, MAX_QUEUE, azs_info[str(k)]['max'],
                      GASOLINE_BRANDS, *(azs_info[str(k)]['oil']),
                      '->', '*' * evaluation_num[k])

        if i in its_time_to_go.values():
            for n, m in its_time_to_go.items():
                if m == i:
                    for o, p in evaluation_list.items():
                        if n in p:
                            evaluation_list[o].remove(n)
            g = 0
            arrived_with_repeat_departure = []
            lst = list(its_time_to_go.values())
            Lst = list(its_time_to_go.keys())
            for z in range(len(its_time_to_go.keys())):
                if i == lst[z]:
                    g += 1
                    arrived_with_repeat_departure.append(Lst[z])
            for s in range(g):
                arrive = arrived_with_repeat_departure[s]
                l = clients[arrive]['station']
                evaluation_num[l] -= 1
                print(V, back_time(i), CLIENT, back_time(arrive),
                      clients[arrive]['oil'], clients[arrive]['V'],
                      clients[arrive]['time_to_stop'], FILLED_THE_CAR)
                for k in range(1, value + 1):
                    print(MACHINE_NUMBER, k, MAX_QUEUE, azs_info[str(k)]['max'], GASOLINE_BRANDS,
                          *(azs_info[str(k)]['oil']),
                          '->', '*' * evaluation_num[k])
                its_time_to_go.pop(arrive)

    print(TOTAL_SOLD_LITRES)
    for key in queue_col:
        print(key, ':', queue_col[key], sep='')
    money = 0
    our_patrol = [AI_80, AI_92, AI_98, AI_95]
    for p in our_patrol:
        money += queue_col[p] * price_oil_dict[p]
    print(TOTAL_REVENUE, money)
    print(LEFT_AZS, queue)

                      
if __name__ == '__main__':
    main()
