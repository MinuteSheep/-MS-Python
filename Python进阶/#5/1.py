class Teacher:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def talk(self):
        print('I am {}'.format(self.name))

    @staticmethod
    def is_man(gender):
        if gender == 'male':
            return 1
        return 0
