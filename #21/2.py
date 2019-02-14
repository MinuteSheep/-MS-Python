name = 'MinuteSheep'
print(name)

try:
    print(age)
except NameError:
    print('我是NameError')
except KeyError:
    print('我是KeyError')
