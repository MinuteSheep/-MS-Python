class Doctor():
    def __init__(self, name):
        print('我是第二个被运行的')
        self.name = name

    print('先运行我')

    def talk(self):
        print('只有调用我时才运行我')


lisi = Doctor('male')

lisi.talk()
