
import random
import time


def get_ticket():

    base_str = 'qwertyuiopasdfghjklzxcvbnm'
    ticket = ''

    for i in range(20):

        ticket += random.choice(base_str)

    ticket = 'TK_' + str(int(time.time())) +ticket

    return ticket

