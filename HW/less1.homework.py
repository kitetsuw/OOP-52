class Hero:
    def __init__(self, name, lvl, hp ):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мой уровень {self.lvl}, мое hp:{self.hp}")

    def is_adult(self):
        if self.hp <= 10:
            print(True)
        else:
            print(False)

mider = Hero("Selena", 25, 10)
tank = Hero("Rocksberg", 15, 55)

Hero.introduce(mider)
Hero.is_adult(mider)
Hero.is_adult(tank)
