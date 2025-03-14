from random import randint

class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} делает какое-то действие.")

    def attack(self):
        print(f"{self.name} атакует врага.")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision > 50:
                print(f"{self.name} успешно атакует врага. Оставшиеся стрелы: {self.arrows}")
            else:
                print(f"{self.name} неудачно атакует врага. Оставшиеся стрелы: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать, так как у него нет стрел.")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдыхает и восстанавливает 5 стрел. Текущий запас стрел: {self.arrows}\n")

    def status(self):
        return (f"Имя: {self.name}, Здоровье: {self.hp} \nСтрелы: {self.arrows}, Точность: {self.precision}")

pre_luck = randint(1, 100)
gerald_archer = Archer("Геральд", 90, 4, pre_luck)

gerald_archer.attack()
gerald_archer.attack()
gerald_archer.attack()

gerald_archer.rest()
print(gerald_archer.status())
