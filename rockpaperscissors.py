import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices: # if player doesnt pick from choices keeps asking user
        player = input("rock, paper, or scissors?: ").lower() # any input would work for rock paper and scissors

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lost!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You loose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You loose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")

    play_again=input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye")

