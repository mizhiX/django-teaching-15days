
import random
import time

def get_ticket():
    # 获取ticket
    base_str = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    ticket = ''
    for i in range(30):
        ticket += random.choice(base_str)
    ticket = 'TK_' + str(int(time.time())) + ticket

    return ticket
