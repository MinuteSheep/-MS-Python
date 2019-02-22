class Doctor:
    '''
    类中函数体内的访问
    '''

    def talk(self):
        self.sentence = 'I am man'    # 初始化实例变量self.sentence
        print(self.sentence)


lisi = Doctor()

lisi.talk()  # 调用talk方法
