from time import sleep
from player import Player 
import getpass

class Human(Player):
    def __init__(self, second_player_name ):
        super().__init__(player_name="Player One")
        self.second_player_score = 0
        self.second_player_name = second_player_name

    def player_vs_player(self):
        gesture_list = ["Rock", "Papar", "Scissor", "Lizard", "Spock"]
        
        while self.player_score < 2 and self.second_player_score < 2:

            gestures = [
            (f"{self.player_name}'s score: {self.player_score}"),
            (f"{self.second_player_name}'s score:{self.second_player_score}\n"),
            "0 for Rock",
            "1 for Paper", 
            "2 for Scissors", 
            "3 for Lizard", 
            "4 for Spock\n"
                
            ]
            for num in gestures:
                print(num)
                sleep(1)



            player_choice = getpass.getpass(f"{self.player_name}, choose a gesture: ")
            second_player_choice = getpass.getpass(f"{self.second_player_name}, choose a gesture: ")

            # 0 > 2 and 3
            # 0 < 1 and 4
            if player_choice == "0":
                print(f"{self.player_name} has picked {gesture_list[0]}")
                if second_player_choice == "0":
                    print(f"{self.second_player_name} has also picked {gesture_list[0]}")
                    print("It is a tie.")
                elif second_player_choice == "2":
                    print(f"{self.second_player_name} has picked {gesture_list[2]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1
                elif second_player_choice == "3":
                    print(f"{self.second_player_name} has picked {gesture_list[3]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1

                elif second_player_choice == "1":
                    print(f"{self.second_player_name} has picked {gesture_list[1]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
                elif second_player_choice == "4":
                    print(f"{self.second_player_name} has picked {gesture_list[4]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1

            # 1 > 0 and 4
            # 1 < 2 and 3
            elif player_choice == "1":
                print(f"{self.player_name} has picked {gesture_list[1]}")
                if second_player_choice == "1":
                    print(f"{self.second_player_name} has also picked {gesture_list[1]}")
                    print("It is a tie.")
                elif second_player_choice == "0":
                    print(f"{self.second_player_name} has picked {gesture_list[0]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1
                elif second_player_choice == "4":
                    print(f"{self.second_player_name} has picked {gesture_list[4]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1

                elif second_player_choice == "2":
                    print(f"{self.second_player_name} has picked {gesture_list[2]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
                elif second_player_choice == "3":
                    print(f"{self.second_player_name} has picked {gesture_list[3]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
            

            
            # 2 > 1 and 3
            # 2 < 0 and 4
            elif player_choice == "2":
                print(f"{self.player_name} has picked {gesture_list[2]}")
                if second_player_choice == "2":
                    print(f"{self.second_player_name} has also picked {gesture_list[2]}")
                    print("It is a tie.")
                elif second_player_choice == "1":
                    print(f"{self.second_player_name} has picked {gesture_list[1]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1
                elif second_player_choice == "3":
                    print(f"{self.second_player_name} has picked {gesture_list[3]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1

                elif second_player_choice == "0":
                    print(f"{self.second_player_name} has picked {gesture_list[0]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
                elif second_player_choice == "4":
                    print(f"{self.second_player_name} has picked {gesture_list[4]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1

            # 3 > 1 and 4
            # 3 < 0 and 2
            elif player_choice == "3":
                print(f"{self.player_name} has picked {gesture_list[3]}")
                if second_player_choice == "3":
                    print(f"{self.second_player_name} has also picked {gesture_list[3]}")
                    print("It is a tie.")
                elif second_player_choice == "1":
                    print(f"{self.second_player_name} has picked {gesture_list[1]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1
                elif second_player_choice == "4":
                    print(f"{self.second_player_name} has picked {gesture_list[4]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1

                elif second_player_choice == "0":
                    print(f"{self.second_player_name} has picked {gesture_list[0]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
                elif second_player_choice == "2":
                    print(f"{self.second_player_name} has picked {gesture_list[2]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
                

            # 4 > 0 and 2
            # 4 < 1 and 3
            elif player_choice == "4":
                print(f"{self.player_name} has picked {gesture_list[2]}")
                if second_player_choice == "4":
                    print(f"{self.second_player_name} has also picked {gesture_list[2]}")
                    print("It is a tie.")
                elif second_player_choice == "0":
                    print(f"{self.second_player_name} has picked {gesture_list[1]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1
                elif second_player_choice == "2":
                    print(f"{self.second_player_name} has picked {gesture_list[3]}")
                    print(f"{self.player_name} WIN!")
                    self.player_score += 1

                elif second_player_choice == "1":
                    print(f"{self.second_player_name} has picked {gesture_list[0]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
                elif second_player_choice == "3":
                    print(f"{self.second_player_name} has picked {gesture_list[4]}")
                    print(f"{self.second_player_name} WINS!!")
                    self.second_player_score += 1
            else:
                print("That's not an option. Pick again.")


    