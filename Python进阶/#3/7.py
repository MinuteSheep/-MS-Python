class Doctor:
    '''
    类外访问实例变量
    '''

    def talk(self):
        self.sentence = 'I am man'    # 初始化实例变量self.sentence


lisi = Doctor()

lisi.talk()
print(lisi.sentence)
