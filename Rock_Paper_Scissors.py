import random

while True:
    choices = ["rock", "paper", "scissors"]

    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?:").lower()

    if player == cpu:
        print("cpu: ", cpu)
        print("player:", player)
        print("Tie!")

    elif player == "rock":
        if cpu == "paper":
            print("cpu: ", cpu)
            print("player:", player)
            print("You lose!")
        if cpu == "scissors":
            print("cpu: ", cpu)
            print("player:", player)
            print("You win!")

    elif player == "scissors":
        if cpu == "rock":
            print("cpu: ", cpu)
            print("player:", player)
            print("You lose!")
        if cpu == "paper":
            print("cpu: ", cpu)
            print("player:", player)
            print("You win!")

    elif player == "paper":
        if cpu == "scissors":
            print("cpu: ", cpu)
            print("player:", player)
            print("You lose!")
        if cpu == "rock":
            print("cpu: ", cpu)
            print("player:", player)
            print("You win!")
    
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")