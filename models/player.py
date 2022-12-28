
from typing import List, Optional

from models.card import Card

class Player:
    
    name : str
    
    coins : int
    religion : str
    card1 : Optional[Card]
    card2 : Optional[Card]
    
    def __init__(self, name, religion = None):
        self.name = name
        self.religion = religion
    
    def possible_actions():
        pass

    def action(self, character):
        pass


# class Bot(Player):

#     def __init__():
#         pass