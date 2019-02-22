class Doctor:
    salary = 100

    def talk(self):
        print('I am a doctor')


print(salary)

# salary是Doctor的类变量，在类中定义
# 但在主程序中并不能被正确访问
# 因为salary变量是局部变量
