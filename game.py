from hero import *
from enemy import *
from readchar import readkey, key
import random
import time

class Game:
    def __init__(self):
        self.status = False
        self.rounds = 0
        self.hero = None
        self.slain_enemies = 0
    
    def start_menu_decider(self):
        print("You have the option to:\n" \
        "[I]nspect your here\n" \
        "[S]tart the battle!\n" \
        "[E]xit the game")
        k = readkey()
        if k == "i" or k == "I":
            self.inspect_hero()
        elif k == "s" or k =="S":
            self.start_battle()
        elif k == "e" or k == "E":
            self.end_game()
    
    def inspect_hero(self):
        self.hero.hero_reset()
        print(self.hero)
        self.start_menu_decider()


    def upgrade_equipment_prompt(self):
        print("[W]eapon upgrade\n[A]rmor upgrade")
        k = readkey()
        if k == "w" or k == "W":
            self.hero.weapon.upgrade_tier()
            self.start_menu_decider()
        elif k == "a" or "A" == k:
            self.hero.armor.upgrade_armor()
            self.start_menu_decider()
        

    def start_battle(self):
        self.hero.hero_reset()
        self.rounds += 1
        print("You have entered a battle. Good luck!")
        
        match self.slain_enemies:
            case 0:
                enemy = Viper(10, 5, 3)
                self.simulate_battle(enemy)
            case 1:
                self.hero.health += 10
                enemy = BigUglyBear(15, 15, 8)
                self.simulate_battle(enemy)
            case 2:
                self.hero.health += 20
                enemy = Spider("Disgusting Spider", 45, 10, 12)
                self.simulate_battle(enemy)
            case 3:
                self.hero.health += 30
                enemy = Knight("Dark Knight", 100, 30, 15)
                self.simulate_battle(enemy)
            case 4:
                self.hero.health += 50
                enemy = Dragon("Dragon", 200, 50, 25)
                self.simulate_battle(enemy)
    
    def simulate_battle(self, enemy):
        dead_hero = False
        dead_enemy = False
        random.seed()
        while (not dead_hero and not dead_enemy):
            print("------------------------------------")                

            enemy.attack(self.hero) 
            print(f"You now have {self.hero.health} health and {self.hero.armor.value} armor left")                        
            
            dead_hero = self.hero_is_dead()
            if dead_hero:
                print("------------------------------------")  
                print(f"You died. {enemy.name} killed you. Unfortunately...\n" \
                    f"You have tried {self.rounds} round so far. \n" \
                    "Good news is you can upgrade an item!!")
                self.upgrade_equipment_prompt()
                break
        
            self.hero.attack(enemy)
            print(f"{enemy.name} now have {enemy.health} health and {enemy.armor} armor left")
            dead_enemy = self.enemy_is_dead(enemy)

            time.sleep(1)  
        
        if dead_enemy:
            print("------------------------------------")  
            self.slain_enemies += 1
            print(f"You have defeated {enemy.name}! Congratulations! \n" \
                f"It only took {self.rounds} rounds to get this far!\n")
            self.start_menu_decider() 


    def hero_is_dead(self):
        if self.hero.health > 0:
            return False
        else:
            return True
    
    def enemy_is_dead(self, enemy):
        if enemy.health > 0:
            return False
        else:
            return True
    

    def print_welcome_message(self):
        self.hero = Hero()
        print("Hello and welcome to this CLI autobattler adventure!\n" \
        "You are about to battle your way through 5 monsters!\n" \
        "How many rounds will it take?")
        self.hero.set_name(input("Firstly, what is your name, hero?\n"))
        print(f"Well hello {self.hero.name}! Ready to get started?")

    def start_game(self):
        self.status = True
        self.print_welcome_message()

    def end_game(self):
        print("Thanks for playing!!")
        self.status = False
    
