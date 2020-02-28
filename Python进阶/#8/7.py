#!/usr/bin/env python
#-*- coding:UTF-8 -*-


from multiprocessing import Pool

def test(msg):
    print(msg)

if __name__ == '__main__':
    # Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
    # processes: 指定进程数目，默认为计算机核数os.cpu_count()
    # 如果 initializer 不为 None，则每个工作进程将会在启动时调用 initializer(*initargs)。
    # maxtasksperchild 是一个工作进程在它退出或被一个新的工作进程代替之前能完成的任务数量，为了释放未使用的资源。默认的 maxtasksperchild 是 None，意味着工作进程寿与池齐。
    # context 可被用于指定启动的工作进程的上下文。
    pool1 = Pool(4)      # 指定4个进程数
    for i in range(5):
        msg = 'hi ' + str(i)
        pool1.apply(test, (msg,))       # 返回结果前会阻塞，所以结果是顺序的
    pool1.close()                       # close()的作用是关闭进程池，不能向进程池里添加进程了，必须在join()之前
    pool1.join()

    print('分割线'.center(20, '-'))

    pool2 = Pool()      # 指定进程数，默认为计算机核数，我的是4
    for i in range(5):
        msg = 'hello ' + str(i)
        pool2.apply_async(test, (msg,)) # 返回结果前不会阻塞，其结果是无序的，更适合并行工作，返回结果对象，又返回值需要用get()方法取出
    pool2.close()
    pool2.join()

    print('分割线'.center(20, '-'))

    pool3 = Pool()
    pool3.map(test, ['cool ' + str(i) for i in range(5)])   # 结果无序，对于长的迭代对象很消耗内存，对于长的迭代对象推荐使用imap()
    pool3.close()
    pool3.join()

    print('分割线'.center(20, '-'))

    pool4 = Pool()
    pool4.map_async(test, ['hot ' + str(i) for i in range(5)])   # 与map类似，但返回结果对象，需要用get()方法取出
    pool4.close()
    pool4.join()
