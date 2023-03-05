class Card:
  def __init__(self, rank, color):
    self.rank = rank
    self.color = color

  def __str__(self):
    return self.color + " " + self.rank

  def __repr__(self):
    return self.color + " " + self.rank