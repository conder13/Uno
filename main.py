from deck import Deck
from card import Card
from hand import Hand
import time
import random
deck = Deck()
deck.shuffle()

print("Let's play Uno!")
time.sleep(3)
print("\nYour hand:")

player = Hand()
player.start_hand(deck)
cards_drawn = 0
for i in range(7):
  print(player.cards_in_hand[cards_drawn])
  cards_drawn += 1
  time.sleep(1)
time.sleep(3)
print("\nThe computer has drawn their cards. Ready to play?\n\n")
computer = Hand()
computer.start_hand(deck)
pile = []
starting_card = deck.draw()
pile.append(starting_card)
time.sleep(2)
print("\n\n\nIt is your turn!\n\nMiddle card:\n" + str(pile[0]))
time.sleep(1)
while len(player.cards_in_hand) > 0 and len(computer.cards_in_hand) > 0:
  print("\nChoose a card to put down!")
  time.sleep(0.5)
  output = ""
  for i in range(len(player.cards_in_hand)):
    output += str(i) + ". " + str(player.cards_in_hand[i]) + "\n"
  print(output)
  time.sleep(1)
  choice = input("Choose a card > ")

  
  if player.cards_in_hand[int(choice)].rank == "+2":
    for i in range(2):
      computer.cards_in_hand.append(deck.draw())
    print("The computer picked 2 cards")
      
  while player.cards_in_hand[int(choice)].rank != pile[0].rank and player.cards_in_hand[int(choice)].color != pile[0].color:
    
    if player.cards_in_hand[int(choice)].color == "+4":
      wild_color = input("You played a wild +4, what color do you want to change it to?")
      player.cards_in_hand[int(choice)].color = wild_color
      for i in range(4):
        computer.cards_in_hand.append(deck.draw())
      print("The computer drew 4 cards.")
      break
    if player.cards_in_hand[int(choice)].rank == "Wild":
      wild_color = input("You played a wild, what color do you want to change it to?")
      player.cards_in_hand[int(choice)].color = wild_color
      break
    
    choice = input("\nYou can't play that card! Please choose a different card, or draw a card > ")
    while choice == "draw":
      new_card = deck.draw()
      print("\nYou picked a",new_card)
      player.cards_in_hand.append(new_card)
      time.sleep(1.5)
      if new_card.rank == pile[0].rank or new_card.color == pile[0].color:
        choice = player.cards_in_hand.index(new_card)
      else:
        print("\nThat cards not playable, press enter to draw again!")
        draw_again = input()


  pile[0] = player.cards_in_hand[int(choice)]
  player.cards_in_hand.pop(int(choice))
  print("\nYou put down a " + str(pile[0]))


  computer_playable_cards = []
  for item in computer.cards_in_hand:
    if item.rank == pile[0].rank or item.color == pile[0].color or item.rank == "Wild":
      computer_playable_cards.append(item)
     # if computer doesn't have a playable card, draw until play can happen
  comp_drawn_cards = 0
  while len(computer_playable_cards) == 0:
    print("The computer is drawing...")
    new_comp_card = deck.draw()
    computer.cards_in_hand.append(new_comp_card)
    comp_drawn_cards +=1  
    if new_comp_card.rank == pile[0].rank or new_comp_card.color == pile[0].color:
      computer.cards_in_hand.append(new_comp_card)
      computer_playable_cards.append(new_comp_card)
      print("The computer drew",str(comp_drawn_cards),"cards.")
  #print(computer_playable_cards)
  
  if computer_playable_cards[0].rank == "Wild":
    computer_playable_cards[0].color = random.choice(["Blue","Green","Red","Yellow"])
  if computer_playable_cards[0].rank == "+2":
    for i in range(2):
      player.cards_in_hand.append(deck.draw())
    print("The computer forced you to draw 2 cards.")
  pile[0] = computer_playable_cards[0]
  computer.cards_in_hand.remove((computer_playable_cards[0]))
  computer_playable_cards = []
  time.sleep(2)
  print("\nThe Computer put down a", str(pile[0]))
  time.sleep(2)
