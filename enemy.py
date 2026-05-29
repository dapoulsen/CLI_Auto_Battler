import random

class Enemy:

    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def basic_attack(self, enemy):
        if enemy.armor.value >= 0 and enemy.armor.value - self.damage >= 0:
            enemy.armor.value -= self.damage
        elif enemy.armor.value >= 0:
            health_dmg = self.damage - enemy.armor.value
            enemy.armor.value = 0
            enemy.health -= health_dmg
        else:
            enemy.health -= self.damage

        print(f"{self.name} does a basic attack on {enemy.name} dealing {self.damage} damage!")
    
    def attack(self, enemy):
        self.basic_attack(enemy)

class Viper(Enemy):
    def __init__(self, health, armor, damage):
        super().__init__("Viper", health, armor, damage)
    
    def bite_attack(self, enemy):
        print(f"{self.name} bites {enemy.name} for {self.damage + 2} damage")
        enemy.health -= self.damage + 2
    
    def attack(self, enemy):
        if random.randint(0, 10) > 7:
            self.bite_attack(enemy)
        else:
            self.basic_attack(enemy)