class Doctor:
    '''
    在类中函数体外访问类变量salary
    '''
    salary = 100
    print(salary)

    def talk(self):
        print('I am a doctor')


lisi = Doctor()
