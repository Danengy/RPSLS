from ai import AI
from human import Human
from time import sleep

from player import Player
class Game:

    def __init__(self):
        self.player = Player("Player  One")
        self.ai = AI("Ai")
        self.second_player = Human("Second Player")
        
        
        
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.battle_phase()

        
    def display_welcome(self):
        print("\nWelcome to a game of Rock, Paper, Scissors, Lizard, Spock!")

    def display_rules(self):

        user_input = input("Are you ready to play? Enter y/n: ")
        if user_input == "y":

            rules = [
            "Get ready for an intense game of RPSLS!\n",

            "Here are the rules: \n",

            "Each match will be best out of three. ",
            "Rock crushes Scissors",
            "Scissors cuts Paper",
            "Paper covers Rock",
            "Rock crushes Lizard",
            "Lizard poisons Spock",
            "Spock smashes Scissors",
            "Scissors decapitates Lizard",
            "Lizard eats Paper",
            "Paper disproves Spock",
            "Spock vaporizes Rock\n ",

            "0 for Rock",
            "1 for Paper", 
            "2 for Scissors", 
            "3 for Lizard", 
            "4 for Spock\n"
            ]
            for r in rules:
                print(r)
                sleep(1)

        elif user_input == "n":
            print("That's too bad. Have a great day.")
            


    def battle_phase(self):
        
        user_input = input("How many players? 1 or 2?: ")
        if user_input == "1":
            print("You wil be going up against out best AI. Get ready.")
            self.ai.player_vs_ai()
            
        elif user_input== "2":
            print(f"You will be up against another player.")    
            self.second_player.player_vs_player()
    
    