
from typing import List
import random

from models.card import Card
from models.player import Player

class Game:
    
    players : List[Player] # List of players
    
    n_card : int # Number of each card type in the game
    cards : List[Card] # List of cards in deck

    ambassador : bool # If it's an ambassador game or an Inquisitor game
    religion : bool # If the game should use religion

    turns : int # Number of turns

    def __init__(self, players, ambassador = True):
        # Set the players list
        self.players = players
        
        # Set the total number of cards in the deck
        if(len(self.players) < 3):
            # print("Número insuficiente de jogadores.")
            raise Exception("Número insuficiente de jogadores.")
        elif(len(self.players) >= 3 and len(self.players) <= 6):
            self.n_card = 3
        elif(len(self.players) <= 8):
            self.n_card = 4
        elif(len(self.players) <= 10):
            self.n_card = 5
        else:
            # print("Número de jogadores excedido (>10).")
            raise Exception("Número limite de jogadores excedido.")

        self.ambassador = ambassador

        self.__set_religion()
        print("Religiões criadas.")
        
        self.__create_cards()
        print("Cartas criadas.")

        self.deal_cards()
        print("Cartas distribuídas.")

        self.turns = 0
    
    def __create_cards(self):
        '''
            Creates the deck of cards
            The ambassador game is set by default (ambassador = False for Inquisitor)
        '''
        
        # Declare which cards will be used in the game
        card_types = ["duke", "assassin", "countess", "captain"]
        if(self.ambassador):
            card_types.append("ambassador")
        else:
            card_types.append("inquisitor")
        
        # Creates the deck of cards
        self.cards = card_types * self.n_card
        
        # Shuffle the cards
        random.shuffle(self.cards)
        
    def deal_cards(self):
        '''
            Creates the deck of cards and handle them randomly across all players    
        '''
    
        for player in self.players:
            player.card1 = self.cards.pop()
            player.card2 = self.cards.pop()
    
    def __set_religion(self):

        if(self.players[0].religion is not None and self.players[0].religion in ["catholic", "protestant"]):
            base_religion = self.players[0].religion
        else:
            base_religion = random.choice(["catholic", "protestant"])

            if(base_religion == "catholic"):
                side_religion = "protestant"
            else:
                side_religion = "catholic"

            for i in range(len(self.players)):
                if(i % 2 == 0):
                    self.players[i].religion = base_religion
                else:
                    self.players[i].religion = side_religion

    def start(self):
        while(not self.end_game()):
            self.turns += 1
            pass

    def end_game(self):
        self.turns += 1
        print("Turno {}".format(self.turns))

        if(self.turns >= 5):
            print("Fim de jogo.")
            return True
        
        return False