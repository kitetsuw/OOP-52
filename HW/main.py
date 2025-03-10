'''import my_module as md
from my_module import add, subtrakt
print(md.add(3, 2))
print(subtrakt(7, 2))
'''
import random
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.__random_int = random.randint(1, 3)

    def attack(self):
        print(f"{self.name} атакует базавой атакой {self.power}!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье до {self.health} HP!")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
