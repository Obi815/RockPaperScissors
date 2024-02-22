import random

options = ('ROCK', 'PAPER', 'SCISSORS')

player = None
computer = random.choice(options)

while player not in options:
    player = input("Rock Paper or Scissors?: ").upper()

print("Player: " + player) 
print("Computer: " + computer)

if player == computer:
    print("It is a tie")