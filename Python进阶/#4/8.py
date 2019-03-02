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

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def smell(self):
        print('狗的嗅觉灵敏')

    def eat(self):
        '''
        改写超类eat方法
        '''
        print('吃肉！')


dog = Dog('wangwang', 5, 'male')  # 实例化dog
print(dog.name)
print(dog.age)
print(dog.gender)
dog.eat()
