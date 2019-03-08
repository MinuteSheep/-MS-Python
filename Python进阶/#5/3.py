class Teacher(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @staticmethod
    def is_man(gender):
        if gender == 'male':
            return 1
        return 0

    def eat(self):
        flag = self.is_man(self.gender)   # 作为全局配置使用
        if flag:
            print('I am {}, I will eat 2 buns'.format(flag))
        else:
            print('I am {}, I will eat 1 bun'.formar(flag))


class Chinese(Teacher):
    '''
    创建一个语文老师类，
    继承Teacher
    '''

    def __init__(self, name, gender):
        super().__init__(name, gender)

    @staticmethod
    def is_man(gender):
        if gender == 'male':
            return 'man'
        return 'woman'


zhangsan = Chinese('zhangsan', 'male')

zhangsan.eat()
