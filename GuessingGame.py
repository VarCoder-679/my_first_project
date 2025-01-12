#------------->Guessing Game in Python
import random
low_numb = 1
high_numb = 100

answer = random.randint(low_numb, high_numb)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low_numb} and {high_numb}")

while is_running:
    guess = input("Enter the guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess< low_numb or guess > high_numb:
            print("OUT OF RANGE!")
        elif guess < answer:
            print("TOO LOW!")
        elif guess> answer:
            print("TOO HIGH!")

        else:
            print(f"CORRECT! The answer was: {answer}")
            print(f"Number of guesses: {guesses}")
            break
    else:
        print("Invalid Guess")
print("END")
