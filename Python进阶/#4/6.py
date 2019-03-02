class Animal:
    '''
    所有动物的超类
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('动物都会吃饭')

    def talk(self):
        print('动物都会叫')


class Dog(Animal):
    '''
    继承Animal
    '''

    def smell(self):
        print('狗的嗅觉灵敏')

    def eat(self):
        '''
        改写超类eat方法
        '''
        print('吃肉！')


dog = Dog('wangwang',5)  # 实例化dog

dog.eat()
