#Множественное наследование
class Animal:
    def action(self):
        return print("some action")

class Flyable(Animal):
    def action(self):
        return print("fly")                                #Animal
                                                #Flyable               #Swimmable
class Swimmable(Animal):                                  #Duck
    def action(self):
        return print("swim")

class Duck(Swimmable, Flyable):
    def make_sound(self):
        return print("Krya Krya")

donald_duck = Duck()
donald_duck.action()
donald_duck.make_sound()



# -------- Big O нотация --------
# Это способ описания сложности алгоритмов

