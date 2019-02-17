import time    # 引入time模块，这是一个时间模块，以后会讲到


def tell_name():
    start_time = time.time()
    print('I am MinuteSheep')
    time.sleep(2)  # 为了体现执行时间，让程序等两秒
    end_time = time.time()
    print('执行时间为：', end_time - start_time)


tell_name()
