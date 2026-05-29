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

    def normal_attack(self, enemy, dmg):
        if enemy.armor.value >= 0 and enemy.armor.value - self.damage >= 0:
            enemy.armor.value -= dmg
        elif enemy.armor.value >= 0:
            health_dmg = dmg - enemy.armor.value
            enemy.armor.value = 0
            enemy.health -= health_dmg
        else:
            enemy.health -= dmg
    
    def attack(self, enemy):
        self.basic_attack(enemy)

class Viper(Enemy):
    def __init__(self, health, armor, damage):
        super().__init__("Viper", health, armor, damage)
    
    def bite_attack(self, enemy):
        print(f"{self.name} bites {enemy.name} for {self.damage + 2} damage")
        enemy.health -= self.damage + 2

    def normal_attack(self, enemy, dmg):
        return super().normal_attack(enemy, dmg)
    
    def attack(self, enemy):
        if random.randint(0, 10) > 7:
            self.bite_attack(enemy)
        else:
            self.basic_attack(enemy)

class BigUglyBear(Enemy):
    def __init__(self, health, armor, damage):
        super().__init__("BUB", health, armor, damage)

    def normal_attack(self, enemy, dmg):
        return super().normal_attack(enemy, dmg)
    
    def claw_attack(self, enemy):
        dmg = self.damage * 1.5
        self.normal_attack(enemy, dmg)
        print(f"{self.name} swings claws at {enemy.name} for {dmg} damage")
    
    def weak_attack(self, enemy):
        dmg = self.damage // 2
        self.normal_attack(enemy, dmg)
        print(f"{self.name} falls over and only scratches {enemy.name} for {dmg}")
    
    def attack(self, enemy):
        randnum = random.randint(0, 100)
        if randnum < 30 and randnum > 90:
            self.claw_attack(enemy)
        elif randnum >= 30 and randnum <= 90:
            self.basic_attack(enemy)
        else:
            self.weak_attack(enemy)

class Spider(Enemy):
    def __init__(self, name, health, armor, damage):
        super().__init__(name, health, armor, damage)
    
    def attack(self, enemy):
        return super().attack(enemy)
    
    def normal_attack(self, enemy, dmg):
        return super().normal_attack(enemy, dmg)

class Knight(Enemy):
    def __init__(self, name, health, armor, damage):
        super().__init__(name, health, armor, damage)

    def normal_attack(self, enemy, dmg):
        return super().normal_attack(enemy, dmg)

    def double_attack(self, enemy):
        dmg = self.damage * 2
        self.normal_attack(enemy, dmg)
        print(f"{self.name} charges with his horse and hits {enemy.name} for {self.damage} damage\n" \
              f"{self.name} is too fast! {enemy.name} is attacked again for {self.damage} damage")
    
    def armor_up(self):
        print(f"{self.name} polishes his armor, gaining an additional 25 armor")
        self.armor += 25
    
    def attack(self, enemy):
        randnum = random.randint(0, 100)
        if randnum < 20:
            self.armor_up()
        elif randnum > 85:
            self.double_attack(enemy)
        else:
            self.basic_attack(enemy)

class Dragon(Enemy):
    def __init__(self, name, health, armor, damage):
        super().__init__(name, health, armor, damage)

    def normal_attack(self, enemy, dmg):
        return super().normal_attack(enemy, dmg)

    def attack(self, enemy):
        randnum = random.randint(0, 100)
        if randnum <= 2:
            self.miss(enemy)
        elif randnum > 2 and randnum <= 70:
            self.basic_attack(enemy)
        elif randnum > 70 and randnum <= 80:
            self.armor_melt(enemy)
        else:
            self.piercing_bite(enemy)
        
    def armor_melt(self, enemy):
        print(f"{self.name}'s breath melts ALL of {enemy.name}'s armor!")       
        enemy.armor.value = 0
    
    def piercing_bite(self, enemy):
        print(f"{self.name} bites {enemy.name} ignoring the armor, dealing {self.damage} damage")
        enemy.health -= self.damage
    
    def miss(self, enemy):
        print(f"{self.name} flies towards {enemy.name}. {enemy.name} epically dodges the attack!")
    
    
