# Наследование

# Полиморфизм

# Родительский класс / Супер /Базовый класс
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return print(f"Я {self.name}, мой уровень {self.lvl}")

    def action(self):
        return print(f"{self.name} выполняет базовое действие")

#CamelCase - Верблюжая нотация - UpperCamelCase & lowerCamelCase
# Дочерний классном
class WarriorHero(Hero):

    def __init__(self,name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 1
            return print(f'{self.name} атакует мечом!')
        else:
            return print(f'{self.name} мало стамины!')

#    def introduce(self):
#        return print(f"Name:{self.name}, ST{self.st}")

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

#snake_case = змеиная нотация
kirito_hero = WarriorHero("Kirito", 100, 1000, 10)
gandalf_hero = MageHero("Gandalf", 100, 1000, 10)

kirito_hero.action()
kirito_hero.introduce()
kirito_hero.attack()
gandalf_hero.introduce()
