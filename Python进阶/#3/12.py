class Doctor:

    def talk(self):
        salary = 100
        print(salary)

    def eat(self):
        print(salary)


lisi = Doctor()
lisi.talk()
lisi.eat()

# 在类中talk方法里定义局部变量salary
# 在其他方法中是不能被访问的
