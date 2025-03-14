from main import Hero

class Jester(Hero):
    def unique_attack(self):
        print(f"{self.name} использует специальную атаку: метает кинжал!")

    def unique_scream(self):
        print(f"{self.name} сказал: 'Ха-ха! Попробуй поймай меня!'")

    def action(self):
        random_value = self.get_random_int()
        if random_value == 1:
            self.attack()
        elif random_value == 2:
            self.protection()
        elif random_value == 3:
            self.rest()

jester = Jester("Шут", 100, 15)
jester.action()
jester.unique_attack()
jester.unique_scream()
