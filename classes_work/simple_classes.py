import datetime


class Superhero:
    def __init__(self, birthday):
        self.birthday = birthday
        pass

    def say_first_name(name):
        print(name)


batman = Superhero(birthday=datetime.date(1999, 11, 19))

print(batman.birthday)


class Superman(Superhero):
    def __init__(self):
        print(self)

clark = Superman()
clark.birthday = datetime.date(1999, 11, 19)
print(clark.birthday.day)

class Batman(Superhero):
    def __init__(self):
        print('rinbirnr')


bat = Batman()
print(bat)