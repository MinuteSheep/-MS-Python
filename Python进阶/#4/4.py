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


class Cat(Animal):
    '''
    继承Animal
    '''

    def tree(self):
        print('猫会爬树')


dog = Dog()  # 实例化dog
cat = Cat()  # 实例化cat

dog.eat()  # dog调用了超类Animal的方法
dog.talk()
dog.smell()  # dog调用自己的smell方法

cat.eat()  # cat也是一样的
cat.talk()
cat.tree()
