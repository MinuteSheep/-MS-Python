# This is a test for ipdb
# Author: MinuteSheep<minutesheep@163.com>

import time
import math


def get_p_time():
    present_time = time.asctime()
    return present_time


a = 123
b = 456

c = a + b

print(c)

present_time = get_p_time()

print(present_time)
