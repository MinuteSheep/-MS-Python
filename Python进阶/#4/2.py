class Doctor():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('My gender is {0}'.format(self.name))


lisi = Doctor('male')

lisi.talk()
