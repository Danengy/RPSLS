from player import Player 
from time import sleep
class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.human_score = 0
        self.name = name

    def player_vs_human(self):
        while self.human_score and self.score < 3:
            player_choice = 



    