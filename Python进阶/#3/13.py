class Doctor:
    salary = 100  # 初始化类变量salary

    def talk0(self):
        print('talk0:', Doctor.salary)
        Doctor.salary = 200   # 修改类变量salary的值为200

    def talk1(self):
        print('talk1:', Doctor.salary)
        print('talk1:', self.salary)
        self.salary = 300   # 修改self.salary的值为300

    def talk2(self):
        print('talk2:', self.salary)
        print('talk2:', Doctor.salary)  # 输出的类变量并没有被改变为300


lisi = Doctor()

lisi.talk0()
lisi.talk1()
lisi.talk2()
