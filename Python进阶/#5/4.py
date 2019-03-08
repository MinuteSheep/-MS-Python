class Teacher(object):
    food = 'bun'

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @classmethod
    def eat(cls):
        print(cls.food)


zhangsan = Teacher('zhangsan', 'male')
zhangsan.eat()
