from card import Card

RANKS = ["1","2","3","4","5","6","7","8","9","10","+2","Skip"]

COLORS = ["Red","Yellow","Green","Blue"]




class Deck:
  def __init__(self):
    self.cards = []
    for color in COLORS:
      for rank in RANKS:
        for i in range(2):
          self.cards.append(Card(rank,color))
    for i in range(8):
      self.cards.append(Card("Wild",""))
    for i in range(4):
      self.cards.append(Card("Wild","+4"))

  def __str__(self):
    for card in self.cards:
      print(card)
    return ""

  def shuffle(self):
    import random
    random.shuffle(self.cards)

  def draw(self):
    return self.cards.pop(0) 
    
    