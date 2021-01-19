import random
import time

print ("Welcome to the blackjack simulator")

King = 10
Queen = 10
Jack = 10
Ace = 1
DealersCards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, King, Queen, Jack]
PlayersCards = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, King, Queen, Jack]
Card1 = 0
Card2 = 0

def play():
     print("""You will receive 2 cards""")
     Card1 =(random.choice(PlayersCards))
     time.sleep(3)
     Card2 =(random.choice(PlayersCards))
     print ("The first card you pulled is {0}".format(Card1),"and the second card you pulled is {0}".format(Card2))
     global Hand1
     time.sleep(3)
     Hand1 = int(Card1) + int(Card2)
     print("The total is",Hand1)

def stand():
    print ("The total you have is ")

def playHouse():
   print("""The dealer receives two cards""")
   CardH1 = (random.choice(PlayersCards))
   time.sleep(3)
   CardH2 = (random.choice(PlayersCards))
   print("The first card the dealer pulled is {0}".format(CardH1), "and the second card the dealer pulled is {0}".format(CardH2))
   global HandH1
   time.sleep(3)
   global HandH1
   HandH1 = int(CardH1) + int(CardH2)
   print("The total is", HandH1)

def hitHouse1():
    if HandH1 <= 21:
        HandHR1 = (random.choice(DealersCards))
        print ("The dealer pulled",HandHR1)
        hitHouse = HandH1 + HandHR1
        print ("The dealer now has",hitHouse)

def hit():
   Hit1 = random.choice(PlayersCards)
   print ("The number you pulled is {0}".format(Hit1))
   global TotalHit
   TotalHit = int(Hand1) + int(Hit1)
   #jason is cute
   print ("The total is now", TotalHit)

def hit2():
   Hit2 = random.choice(PlayersCards)
   print ("The number you pulled is {0}".format(Hit2))
   TotalHit2 = Hit2 + TotalHit
   print ("The total is",TotalHit2)

                                ###Main LOOP###
running = True
while running:
   choice = input("What do you want to do:\nDraw\nhit\nstand\nQuit").lower()
   if choice == "draw":
       play()
       playHouse()
   elif choice == "quit":
       running = False
   elif choice == "hit":
       hit()
       hitHouse1()
       HitAgainOption = input("If you would like to hit again, write yes and if you would like to stand, write stand.")
       if HitAgainOption == "yes":
           hit2()
   #...etc...
   else:
       print("Sorry thats not an option")



#Start = input("Please enter yes if you would like to start.")

#if Start == "yes":
#   play()
