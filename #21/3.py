try:
    print(age)
except (NameError, KeyError):
    print('异常被正确捕捉')
