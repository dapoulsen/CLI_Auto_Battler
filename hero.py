from weapon import *
from armor import *
class Hero:
    def __init__(self):
        self.name = ""
        self.weapon = Weapon()
        self.armor = Armor()
        self.health = 20

    def attack(self, enemy):
        if enemy.armor > 0 and enemy.armor - self.weapon.damage >= 0:
            enemy.armor -= self.weapon.damage
        elif enemy.armor > 0:
            healt_dmg = self.weapon.damage - enemy.armor
            enemy.armor = 0
            enemy.health -= healt_dmg
        else:
            enemy.health -= self.weapon.damage
        
        print(f"{self.name} attacks {enemy.name} with a {self.weapon} dealing {self.weapon.damage} damage")

    def set_name(self, name):
        self.name = name
    
    def hero_reset(self):
        self.health = 20
        self.armor.reset_armor()
    

    def __str__(self):
        return f"{self.name} has {self.health} health. Is wearing {self.armor.show_tier()} armor and uses a {self.weapon.show_tier()} weapon."