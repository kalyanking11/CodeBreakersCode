# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:57:28 2020

@author: kalya
"""
SUITS = ['DIAMONDS', 'SPADES', 'HEARTS', 'CLUBS']
VALUES = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
    
class Card:
    
    def __init__(self, suit, value):
        self.suit_name = suit
        self.value_of_card = value
    def suit(self):
        return self.suit_name
    def value(self):
        return self.value_of_card
    
# c = Card("DIAMONDS","ACE")

# k = c.suit()
# print(k)
