name = input('Please input your name:')    # 输入你的名字

if name == 'MinuteSheep':   # 判断变量name是否为MinuteSheep
    print('Your are MS')    # 条件为真则执行
    print('Your are the best man in the world!')  # 条件为真则执行
else:
    print('Your are not MS')   # 条件为假则执行


flag = True

if flag:    # 判单flag是否为真，也可以写为 if flag == True：
    print('flag is True')
# 条件为假时不需要执行任何代码，则else忽略不写
