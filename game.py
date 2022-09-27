
from time import sleep
class Game:

    def __init__(self) -> None:
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        
    def display_welcome(self):
        print("Welcome to a game of Rock, Paper, Scissors, Lizard, Spock!")

    def display_rules(self):
        user_input = input("Are you ready to play? Enter y/n: ")
        if user_input == "y":
            print("Get ready for an intense game of RPSLS!\n")
            sleep(1.5)
            print("Here are the rules: \n")
            sleep(1)
            rules = [

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
            self.display_options()
        elif user_input == "n":
            print("That's too bad. Have a great day.")


    def ask_for_players(self):
        
        user_input = input("How many players? 1 or 2?")
        if user_input == "1":
            pass
        elif user_input== "2":
            pass
    
    def display_options(self):
        options = ["0 for Rock",
        "1 for Paper", 
        "2 for Scissors", 
        "3 for Lizard", 
        "4 for Spock\n"]
        for num in options:
            print(num)
            sleep(1)


