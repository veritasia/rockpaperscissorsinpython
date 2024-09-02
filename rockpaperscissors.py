import random

userWins = 0
pcWins = 0
choices = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock, Paper, or Scissors or Q to quit ").lower()
    
    if userInput == "q":
        print("Thanks for playing!")
        print("You have a score of " + str(userWins))
        break

    if userInput not in choices:
       print("Please choose a valid type")
       continue

    print("whoaooaoaoa")
    randomNum = random.randint(0,2)
    #rock:0, paper:1, scissors:2
    pcChoice = choices[randomNum]

    print("Computer picked", pcChoice + ".")

    if userInput == pcChoice:
        print("you have a tie!")
        print("No one gets a point")
    elif userInput == "rock" and pcChoice == "scissors":
        print("you win!")
        userWins += 1
    elif userInput == "scissors" and pcChoice == "paper":
        print("you win!")
        userWins += 1
    elif userInput == "paper" and pcChoice == "rock":
        print("you win!")
        userWins += 1
    else:
        print("you lose </3")
        pcWins += 1
    
    print("Your current score is", userWins)
    print("Computer's current score is", pcWins)

print("See you later!")

