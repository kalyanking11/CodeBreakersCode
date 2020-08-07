# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:07:41 2020

@author: kalyan
"""

suits = ["hearts","clubs","spades","diamonds"]
values = ["ace","one","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def suit(self):
        return self.suit
    def value(self):
        return self.value

class Deck:
    # creates a sorted deck of 13 values and 4 suits
    def __init__(self):
        self.new_deck = [suit+"-"+value for suit in suits for value in values]
    def num_card(self):
        return len(self.new_deck)
    def shuffle(self):
        return random.shuffle(self.new_deck)
    def peek(self):
        return self.new_deck[-1]
    def draw(self):
        self.new_deck.pop()
    def add_card(self, card):
        if len(self.new_deck)>52:
            print("The deck is full. Cannot add card")
        else:
            self.new_deck.append(card.suit+"-"+card.value)
    def print_deck(self):
        print(self.new_deck)
        
        