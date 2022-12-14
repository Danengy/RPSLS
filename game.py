from ai import AI
from human import Human
from time import sleep

from player import Player
class Game:

    def __init__(self):
        self.player = Player("Player One")
        self.ai = AI("Ai")
        self.second_player = Human("Second Player")
        
        
    def run_game(self):
        self.display_welcome()
        valid_reponse = False
        while valid_reponse == False:     

            user_input = input("Are you ready to play? Enter y/n: ")
            if user_input == "y":
                self.display_rules()
                self.battle_phase()
                valid_reponse = True
            elif user_input == "n":
                print("That's too bad. Have a good day.")
                break 
            else:
                print("That's not an option. Try again.")
        
    def display_welcome(self):
        print("\nWelcome to a game of Rock, Paper, Scissors, Lizard, Spock!")

    def display_rules(self):

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
        ]
        
        for r in rules:
            print(r)
            sleep(1)

            


    def battle_phase(self):
        
        user_input = input("How many players? 1 or 2?: ")
        if user_input == "1":
            print("You wil be going up against out best AI. Get ready.")
            self.ai.player_vs_ai()
            
        elif user_input== "2":
            print(f"You will be up against another player.")    
            self.second_player.player_vs_player()
        sleep(1)
    