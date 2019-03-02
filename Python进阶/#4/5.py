class Animal:
    '''
    所有动物的超类
    '''

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


dog = Dog()  # 实例化dog

dog.talk()
dog.smell()  # dog调用自己的smell方法
dog.eat()  # 调用被改写的eat方法
