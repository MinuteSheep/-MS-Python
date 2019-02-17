import time    # 引入time模块，这是一个时间模块，以后会讲到


def Time(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            '''
            this is a decorator
            '''
            if num == 1:
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                print('执行时间为：', end_time - start_time)
            elif num == 0:
                func(*args, **kwargs)
                print('不需要计算时间')
        return wrapper
    return decorator


@Time(num=1)
def tell_name(name):
    '''
    tell your name
    '''
    print('I am', name)
    time.sleep(2)  # 为了体现执行时间，让程序等两秒


@Time(num=0)
def add(a, b):
    '''
    add a plus b
    '''
    c = a + b
    print(c)


tell_name('MS')
add(5, 6)
