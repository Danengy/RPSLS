from player import Player
import random
from time import sleep 
class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0 
    
    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        sleep(1)
        print(f"{self.name} has picked {self.gestures[int(self.chosen_gesture)]}")
    


