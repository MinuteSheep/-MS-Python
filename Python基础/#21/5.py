age = 100

try:
    print(age)
except NameError as e:
    print(e)
else:
    print('没有出现异常哦')
