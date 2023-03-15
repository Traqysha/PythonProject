class Animal:
    def __init__(self,name):
        self.myname = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return "Meow"

class Dog(Animal):
    def talk(self):
        return "Woof"

class Horse(Animal):
    def talk(self):
        return "Neigh"

class Donkey(Animal):
    def talk(self):
        return "Bray"

class Cow(Animal):
    def talk(self):
        return "Moo"

paka = Cat("Whiskers")
doggy = Dog("Fido")
farasi = Horse("Dolly")
punda = Donkey("Sammy")
fahali = Cow("Chief")

print(paka.myname + ":" + paka.talk())
print(doggy.myname + ":" + doggy.talk())
print(farasi.myname + ":" + farasi.talk())
print(punda.myname + ":" + punda.talk())
print(fahali.myname + ":" + fahali.talk())