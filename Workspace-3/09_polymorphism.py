class Cat:
    def voice(self):
        print("Meow")


class Dog:
    def voice(self):
        print("Bark")


def voice(x):
    x.voice()


cat = Cat()
dog = Dog()

voice(cat)
voice(dog)
