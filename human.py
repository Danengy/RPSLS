from player import Player 
from time import sleep
class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    
    def choose_gesture(self):
        gesture_list =["Rock", "Papar", "Scissor", "Lizard", "Spock"]
        
        options = [
        "0 for Rock",
        "1 for Paper", 
        "2 for Scissors", 
        "3 for Lizard", 
        "4 for Spock\n"
        ]

        for num in options:
            print(num)
            sleep(1)

        valid_reponse = False
        while valid_reponse == False: 
            user_input = input("Choose the gesture you would like to play: ")
            if user_input == "0":
                print(f"{self.name} have picked {gesture_list[0]}")
                valid_reponse = True
            elif user_input == "1":
                print(f"{self.name} have picked {gesture_list[1]} ")
                valid_reponse = True
            elif user_input == "2":
                print(f"{self.name} have picked {gesture_list[2]} ")
                valid_reponse = True    
            elif user_input == "3":
                print(f"{self.name} have picked {gesture_list[3]} ")
                valid_reponse = True
            elif user_input == "4":
                print(f"{self.name} have picked {gesture_list[4]} ")
                valid_reponse = True
            else:
                print("That's not an option> Please try again.")

    def player_vs_human(self):
        