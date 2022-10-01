class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0

    def choose_gesture(self):
        gesture_list = ["Rock", "Papar", "Scissor", "Lizard", "Spock"]

        valid_reponse = False
        while valid_reponse == False: 
            player_choice = input("Choose the gesture you would like to play: ")
            if player_choice == "0":
                print(f"{self.player_name} has picked {gesture_list[0]}")
                valid_reponse = True
            elif player_choice == "1":
                print(f"{self.player_name} has picked {gesture_list[1]} ")
                valid_reponse = True
            elif player_choice == "2":
                print(f"{self.player_name} has picked {gesture_list[2]} ")
                valid_reponse = True    
            elif player_choice == "3":
                print(f"{self.player_name} have picked {gesture_list[3]} ")
                valid_reponse = True
            elif player_choice == "4":
                print(f"{self.player_name} have picked {gesture_list[4]} ")
                valid_reponse = True
            else:
                print("That's not an option> Please try again.")
