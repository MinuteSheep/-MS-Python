class Doctor:
    '''
    在类外访问类变量salary
    '''
    salary = 100

    def talk(self):
        print('I am a doctor')


lisi = Doctor()
print(Doctor.salary)  # 使用 类.类变量 访问
print(lisi.salary)   # 使用 实例.类变量 访问
