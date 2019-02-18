class Doctor:
    '''
    创建一个医生类
    '''

    def eat(self):
        print('我喜欢吃')

    def talk(self):
        print('我喜欢说话')

    def treat(self):
        print('我喜欢治疗病人')


class Teacher():
    '''
    创建一个老师类
    '''

    def eat(self):
        print('我喜欢吃')

    def talk(self):
        print('我喜欢说话')

    def teach(self):
        print('我喜欢教书')


zhangsan = Teacher()  # 将Teacher类实例化为对象张三
lisi = Doctor()   # 将Doctor类实例化为对象李四

zhangsan.eat()
zhangsan.teach()
lisi.talk()
lisi.treat()
