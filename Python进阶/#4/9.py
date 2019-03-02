class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def eat(self):
        print('{0} eat cat'.format(self.name))


class Cat(Animal):
    def eat(self):
        print('{0} eat mouse'.format(self.name))


class Mouse(Animal):
    def eat(self):
        print('{0} eat {0}'.format(self.name))


def eat(obj):
    obj.eat()


dog = Dog('狗')
cat = Cat('猫')
mouse = Mouse('老鼠')

eat(dog)
eat(cat)
eat(mouse)
