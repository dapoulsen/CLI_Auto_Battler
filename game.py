from hero import *

class Game:
    def __init__(self):
        self.status = False
        self.rounds = 0
        self.hero = None

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