import time    # 引入time模块，这是一个时间模块，以后会讲到


def Time(func):
    def wrapper(name):    # 使用函数的嵌套
        start_time = time.time()
        func(name)
        end_time = time.time()
        print('执行时间为：', end_time - start_time)
    return wrapper


@Time
def tell_name(name):
    print('I am', name)
    time.sleep(2)  # 为了体现执行时间，让程序等两秒


tell_name('MS')  # 相当于执行 wrapper('MS')
