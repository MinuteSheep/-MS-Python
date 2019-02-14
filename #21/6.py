try:
    print(age)
except NameError as e:
    print(e)
else:
    print('没有出现异常')
finally:
    print('最后都得执行我')
