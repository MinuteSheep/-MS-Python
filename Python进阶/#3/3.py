class Doctor:
    '''
    在类中函数体内访问类变量salary
    '''
    salary = 100

    def talk0(self):
        '''
        使用类.类变量访问
        '''
        print('My salary is {0}'.format(Doctor.salary))

    def talk1(self):
        '''
        使用实例.类变量访问
        '''
        print('My salary is {0}'.format(self.salary))


lisi = Doctor()

lisi.talk0()
lisi.talk1()
