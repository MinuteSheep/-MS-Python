#!/usr/bin/env python
#-*- coding:UTF-8 -*-


import os
import time
from multiprocessing import Process


def test(name):
    print(name)

if __name__ == '__main__':
    p1 = Process(target=test, args=('Minute',))       # 参数是元组类型，需要加括号
    p2 = Process(target=test, args=('Sheep',))        # 一个参数必须加逗号,多个则不用

    p1.start()
    p2.start()

    p2.join()
    print('执行完毕')
