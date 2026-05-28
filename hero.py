from weapon import *
class Hero:
    def __init__(self):
        self.name = ""
        self.weapon = Weapon("Basic", 1)
        self.armor = 10
        self.health = 20

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} with a {self.weapon} dealing {self.weapon.damage} damage")
        enemy.health -= self.weapon.damage

    def set_name(self, name):
        self.name = name
