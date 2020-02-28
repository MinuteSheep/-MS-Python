#!/usr/bin/env python
#-*- coding:UTF-8 -*-


import os
import time
from multiprocessing import Process


def test():
    print('Start!')
    print('test 进程ID', os.getpid())
    print('test 父进程ID', os.getppid())
    time.sleep(3)
    print('End!')

if __name__ == '__main__':
    p1 = Process(target=test)       # 创建一个子进程，目标函数为test
    p2 = Process(target=test)       # 创建一个子进程，目标函数为test

    p1.start()
    p2.start()

    print('执行完毕')
    print('main 进程ID', os.getpid())
    print('main 父进程ID', os.getppid())
