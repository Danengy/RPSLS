from player import Player
import random
from time import sleep 
class AI(Player):
    def __init__(self, ai_name ):
        super().__init__(ai_name)
        self.ai_score = 0
        self.ai_name = ai_name 
    
    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Papar", "Scissor", "Lizard", "Spock"]
        sleep(1)
        print(f"{self.ai_name} has picked {gesture_list[int(self.chosen_gesture)]}")
    
    def player_vs_ai(self):
        while True:
            player_choice = Player.choose_gesture()
            ai_choice = self.choose_gesture()

            # 0 > 2 and 3
            # 0 < 1 and 4
            if player_choice == "0":
                if ai_choice == "0":
                    print("It is a tie.")
                elif ai_choice == "2" or "3":
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1 
                elif ai_choice == "1" or "4":
                    print(f"{self.ai_name} WINS!!")
                    self.ai_score += 1

            # 1 > 0 and 4
            # 1 < 2 and 3
            elif player_choice == "1":
                if ai_choice == "1":
                    print("It is a tie.")
                elif ai_choice == "0" or "4":
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1 
                elif ai_choice == "2" or "3":
                    print(f"{self.ai_name} WINS!!")
                    self.ai_score += 1
            
            # 2 > 1 and 3
            # 2 < 0 and 4
            elif player_choice == "2":
                if ai_choice == "2":
                    print("It is a tie.")
                elif ai_choice == "1" or "3":
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1 
                elif ai_choice == "0" or "4":
                    print(f"{self.ai_name} WINS!!")
                    self.ai_score += 1

            # 3 > 1 and 4
            # 3 < 0 and 2
            elif player_choice == "3":
                if ai_choice == "3":
                    print("It is a tie.")
                elif ai_choice == "1" or "4":
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1 
                elif ai_choice == "0" or "2":
                    print(f"{self.ai_name} WINS!!")
                    self.ai_score += 1

            # 4 > 0 and 2
            # 4 < 1 and 3
            elif player_choice == "4":
                if ai_choice == "4":
                    print("It is a tie.")
                elif ai_choice == "0" or "2":
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1 
                elif ai_choice == "1" or "3":
                    print(f"{self.ai_name} WINS!!")
                    self.ai_score += 1

    
