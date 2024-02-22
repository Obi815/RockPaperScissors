import random

options = ('ROCK', 'PAPER', 'SCISSORS')

player = None
computer = random.choice(options)

while player not in options:
    player = input("Rock Paper or Scissors?: ").upper()

print("Player: " + player) 
print("Computer: " + computer)

