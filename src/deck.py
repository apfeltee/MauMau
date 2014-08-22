# -*- coding: utf-8 -*-

import random

#
# This file contains the class for handling the stack and middle in maumau
#


class Deck:

    def __init__(self, name=None):
        english_card_colors = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        english_card_values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        german_card_colors = ['Herz', 'Kreuz', 'Karo', 'Pik']
        german_card_values = ['Zwei', 'Drei', 'Vier', 'Fuenf', 'Sechs', 'Sieben', 'Acht', 'Neun', 'Zehn', 'Bube', 'Dame', 'König', 'Ass']
        self.deck = []
        self.middle_card = ''
        self.deck = self.create_deck(english_card_colors, english_card_values)
        self.middle_card = str(self.deck.pop())

    def create_deck(self, colors, values):
        for i in values:
            for j in colors:
                self.deck.append(i + " of " + j)
                self.randomize_cardstack()
        # debug
        return self.deck

    def get_current_middle(self):
        return str(self.middle_card)

    def middle_to_stack(self):
        self.deck.append(self.middle_card)
        self.middle_card = ''

    def set_new_middle(self, card):
        self.middle_to_stack()
        self.middle_card = card

    def randomize_cardstack(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def card_back_to_stack(self, card):
        self.deck.append(card)
