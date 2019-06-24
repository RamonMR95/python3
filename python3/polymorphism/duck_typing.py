class Duck:

    @staticmethod
    def talk():
        print("CUAK")


class Human:

    @staticmethod
    def talk():
        print("Hi")


def call_talk(obj):
    obj.talk()


d = Duck()
call_talk(d)

h = Human()
call_talk(h)

