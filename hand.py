from card import Card
from deck import Deck

class Hand:
  def __init__(self):
    self.cards_in_hand = []

  def start_hand(self, deck):
    deck.shuffle()
    for i in range(7):
      newcard = deck.draw()
      self.cards_in_hand.append(newcard)
  
  def __repr__(self):
    printout = ""
    for item in self.cards_in_hand:
      printout += str(item)
      printout += "\n"
    return printout
