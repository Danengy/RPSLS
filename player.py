from time import sleep

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def choose_gesture(self):
        gesture_list =["Rock", "Papar", "Scissor", "Lizard", "Spock"]
        
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

    