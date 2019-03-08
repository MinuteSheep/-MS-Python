class Teacher:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def talk(self):
        print('I am {}'.format(self.name))

    @staticmethod
    def is_man(gender):
        if gender == 'male':
            return 1
        return 0

    def eat(self):
        flag = self.is_man(self.gender)   # 作为全局配置使用
        if flag:
            print('I am man, I will eat 2 buns')
        else:
            print('I am woman, I will eat 1 bun')


zhangsan = Teacher('zhangsan', 'male')

zhangsan.eat()
