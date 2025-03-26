from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Flyable():
     def action(self):
          return print("Fly")

class Swimmable(Animal):
     def action(self):
         return print("Swim")

class Dog(Animal):
    def make_sound(self):
        return "gav-gav!"


class Falcon(Dog, Flyable):
    def make_sound(self):
        return "Falcon's scream"

falcon = Falcon()
falcon.action()

animals = [Dog(), Falcon()]
for animal in animals:
    print(animal.make_sound())

