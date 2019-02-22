# 在类中，类变量相当于全局变量
class Doctor:
    salary = 100
    print(salary)

    def talk(self):
        print(Doctor.salary)

    def eat(self):
        print(Doctor.salary)


lisi = Doctor()
lisi.talk()
lisi.eat()

# 因为类变量在整个类中都是共有的
# 因此类变量能被类中的方法访问
# 换句话说，在类中类变量相当于全局变量
