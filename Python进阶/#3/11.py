class Doctor:
    salary = 100
    print(salary)

    def talk(self):
        self.food = 'BaoZi'
        print(Doctor.salary)
        print(self.food)

    def eat(self):
        print(Doctor.salary)
        print(self.food)


lisi = Doctor()
lisi.talk()
lisi.eat()

# 在talk方法里面定义实例变量self.food
# 但是在eat方法里面却可以访问self.food这个实例变量
# 因此，在实例中，类变量和实例变量都相当于全局变量
