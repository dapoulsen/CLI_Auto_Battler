from hero import *
from readchar import readkey, key

class Game:
    def __init__(self):
        self.status = False
        self.rounds = 0
        self.hero = None
    
    def start_menu_decider(self):
        print("You have the option to\n" \
        "[I]nspect your here\n" \
        "[U]pgrade a piece of equipment\n")
        k = readkey()
        if k == "i" or k == "I":
            print("Your inv")
        elif k == "u" or k =="U":
            print("Your upgrade")
    
    def inspect_hero(self):
        pass

    def upgrade_equipment_prompt(self):
        pass

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
    
