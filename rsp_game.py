import random

while True:
    player = input("Choose your move (Rock, Paper, Scissors): ")
    computer = random.choice(["Rock", "Paper", "Scissors"])

    if player == "Rock":
        if computer == "Paper":
            print("Paper covers Rock, computer wins!")
        else:
            print("Congratulations, you win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Scissors cuts Paper, computer wins!")
        else:
            print("Congratulations, you win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer wins!")
        else:
            print("Congratulation, you win!")
    elif player == computer:
        print("Tie!")
    else:
        print("Invalid input!")
    new_game = input("Do you want to play again(yes/no): ")
    if new_game == "yes":
        continue
    else:
        break
