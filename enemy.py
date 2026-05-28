
class Enemy:

    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def basic_attack(self, enemy):
        print(f"{self.name} does a basic attack on {enemy.name} dealing {self.damage} damage!")
        enemy.health -= self.damage

class Viper(Enemy):
    def __init__(self, health, armor, damage):
        super().__init__("Viper", health, armor, damage)
    
    def bite_attack(self, enemy):
        print(f"{self.name} bites {enemy.name} for {self.damage + 2} damage")
        enemy.health -= self.damage + 2