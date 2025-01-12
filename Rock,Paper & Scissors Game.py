#-------->ROCK, PAPER, SCISSORS
import random
options = ['rock', 'paper', 'scissors']
player = 0
#computer = random.choice(options)

while True:
    player = input("Enter the options(rock,paper, scissors): ")

    if player not in options:
        print("INVALID INPUT! Please choose one (rock, paper or scissors)")
        continue  #SKIPS TO NEXT ITERATION OF LOOP

    computer = random.choice(options)
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == 'rock' and computer == 'scissors':
        print("YOU WIN!")
    elif player == 'paper' and computer == 'rock':
        print("YOU WIN!")
    elif player == 'scissors' and computer == 'paper':
        print("YOU WIN!")
    elif player==computer:
        print("TIE!")
    else:
        print("YOU LOSE!")

    play_again = input("Want to play again? (y/n): ").lower()
    if play_again == 'n':
        break         #BREAKS THE LOOP

print("THANKS FOR PLAYING.")
