import random
import sys

userScore = 0
computerScore = 0
tieCounter = 0
cycle = True

def game():
	global userScore
	global computerScore
	global tieCounter

	userChoice = input("Do you choose rock, paper, or scissors? : ")
	
	if userChoice == 'rock' or userChoice == 'Rock':
		userChoice = 1
	elif userChoice == 'paper' or userChoice == 'Paper':
		userChoice = 2
	elif userChoice == 'scissors' or userChoice == 'Scissors':
		userChoice = 3

	computerChoice = random.randrange(1,4,1)

	if computerChoice == 1:
		print("The computer chose Rock.")
	elif computerChoice == 2:
		print("The computer chose Paper.")
	elif computerChoice == 3:
		print("The computer chose Scissors.")

	if userChoice == computerChoice:
		print("It's a tie.")
		tieCounter = tieCounter + 1

	if userChoice == 1 and computerChoice == 2:
		print("The computer wins.")
		computerScore = computerScore + 1
	elif userChoice == 1 and computerChoice == 3:
		print("You win!")
		userScore = userScore + 1
	elif userChoice == 2 and computerChoice == 1:
		print("You win!")
		userScore = userScore + 1
	elif userChoice == 2 and computerChoice == 3:
		print("The computer wins.")
		computerScore = computerScore + 1
	elif userChoice == 3 and computerChoice == 1:
		print("The computer wins.")
		computerScore = computerScore + 1
	elif userChoice == 3 and computerChoice == 2:
		print("You win!")
		userScore = userScore + 1

	print("Overall - You: " + str(userScore) + ". Computer: " + str(computerScore) + ". Ties: " +str(tieCounter) +".")
	

def playAgain():
	question = input("Do you want to play again? ")
	if question == "Yes" or question == "yes":
		print(" ")
	elif question == "No" or question == "no":
		sys.exit()
	else:
		print("I didn't understand. Please enter 'Yes' or 'No'.")
		playAgain()

while cycle == True: 
	game()
	playAgain()

