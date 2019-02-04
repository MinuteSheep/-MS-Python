import time    # 引入time模块，这是一个时间模块，以后会讲到


def tell_name():
    print('I am MinuteSheep')
    time.sleep(2)  # 为了体现执行时间，让程序等两秒


def Time(func):
    def wrapper():    # 使用函数的嵌套
        start_time = time.time()
        func()
        end_time = time.time()
        print('执行时间为：', end_time - start_time)
    return wrapper


tell_name = Time(tell_name)   # 相当于 tell_name = wrapper
tell_name()  # 相当于执行 wrapper()
