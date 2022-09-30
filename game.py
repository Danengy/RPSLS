from ai import AI
from human import Human
from time import sleep
class Game:

    def __init__(self):
        self.ai = AI("AI")
        self.human = Human(int("Enter second player name: "))
        
        

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        
    def display_welcome(self):
        print("Welcome to a game of Rock, Paper, Scissors, Lizard, Spock!")

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
            "Spock vaporizes Rock\n "
            ]

            for r in rules:
                print(r)
                sleep(1)

        elif user_input == "n":
            print("That's too bad. Have a great day.")


    def ask_for_players(self):
        
        user_input = input("How many players? 1 or 2?")
        if user_input == "1":
            print("You wil be going up against out best AI. Get ready.")
            
        elif user_input== "2":
            print()            
    


    




