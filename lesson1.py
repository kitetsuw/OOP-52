class Car:
    #Конструктор класса
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    #Методы класса
    def signal(self):
        print(f"{self.color} car signal")

    def action(self):
        print(f"{self.model} start acton!")


kia = Car("k5", 2023, "white")
kia.signal()
kia.action()

