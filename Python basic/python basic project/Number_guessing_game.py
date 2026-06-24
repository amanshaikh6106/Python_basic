#wap to genrate 1 to 100 the user has to guess the number the program should give hint like too high or too low untill correct guess made

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Try to guess the number between 1 and 100.")


    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Please guess a number within the range 1 to 100.\n")
        elif guess < number_to_guess:
            print("Too low! Try again.\n")
        elif guess > number_to_guess:
            print("Too high! Try again.\n")
        else:
            guessed_correctly = True
            print(f"\nCongratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")


if __name__ == "__main__":
    number_guessing_game()
    