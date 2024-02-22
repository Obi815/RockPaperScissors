import random

print(" ")
print("WELCOME TO ROCK PAPER SCISSORS!!!")
print("---------------------------------")

# set up variables
cpuScore = 0
playerScore = 0 
tieScore = 0
options = ['Rock', 'Paper', 'Scissors']

def checkWinner(playerHand, computerHand):
    if (playerHand == 'Rock' and computerHand == 'Paper'):
        print("Sorry you lost")
        return 'CPU'
    elif(playerHand == 'Rock' and computerHand == 'Scissors'):
        print("Hooray you have won!!")
        return 'Player'
    elif(playerHand == 'Scissors' and computerHand == 'Rock'):
        print("Sorry you lost")
        return 'CPU'
    elif(playerHand == 'Scissors' and computerHand == 'Paper'):
        print("Hooray you have won!!")
        return 'Player'
    elif(playerHand == 'Paper' and computerHand == 'Rock'):
        print("Hooray you have won!!")
        return 'Player'
    elif(playerHand == 'Paper' and computerHand == 'Scissors'):
        print("Sorry you lost")
        return 'CPU'
    else:
        print("It's a tie, play again!")
        return 'Tie'
    
#  Game loop
while(playerScore != 3 and cpuScore != 3):
#  validate input 
    while True:
        playerHand = input("\nPick a hand. Rock, Paper, or Scissors: ")
        if(playerHand == 'Rock' or playerHand == 'Paper' or playerHand == 'Scissors'):
            break
        else:
            print("Invalid input. Try again")
    # Generating Computer Pick
    computerHand = random.choice(options)

    # Print Results
    print("Your hand: " + playerHand)
    print("CPU hand: " + computerHand)
    result = checkWinner(playerHand, computerHand)
    if(result == 'Player'):
        playerScore += 1
    elif(result == "CPU"):
        cpuScore += 1
    else: 
        tieScore += 1
    print("Your Score: ", playerScore, "CPU:", cpuScore, "Ties:", tieScore)

print("Game Over! Thank You for playing :)")



