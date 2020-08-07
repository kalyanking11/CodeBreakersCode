# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:58:04 2020

@author: kalya
"""
from card import SUITS,VALUES,Card
import random
class Deck:
    # creates a sorted deck of 13 values and 4 suits
    def __init__(self):
        self.new_deck = [Card(suit,value) for suit in SUITS for value in VALUES]
        
        
    def num_cards(self):
        if len(self.new_deck) == 0:
            return 'Deck is empty'
        return len(self.new_deck)
    def shuffle(self):
        return random.shuffle(self.new_deck)
    def peek(self):
        if len(self.new_deck) == 0:
            return 'Deck is empty'
        return self.new_deck[-1]
    def draw(self):
        if len(self.new_deck) == 0:
            return 'Deck is empty'
        else:
            self.new_deck.pop()
    def add_card(self, card):
        if len(self.new_deck)>52:
            print("The deck is full. Cannot add card")
        else:
            self.new_deck.append(card)
    def print_deck(self):
        for card in self.new_deck:
            print(card.suit(), card.value())
d = Deck()
d.print_deck()