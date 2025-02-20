import random

def guess_the_number():
    print("\n\nWelcome to DELUXE Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")


    lower_limit = 1
    upper_limit = 100
    max_attempts = 10
    difficulty = input("Choose a difficulty level - Easy,Medium, or Hard:").lower()
    if difficulty == "easy":
        max_attempts = 15
    elif difficulty == "medium":
        max_attempts = 10
    elif difficulty == "hard":
        max_attempts = 5
    else:
        print("Invalid difficulty level.Playing on Medium.")
    secret_number = random.randint(lower_limit,upper_limit)
    attempts = 0
    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts+1}/{max_attempts}:Enter your guess:"))
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts+1} attempts.")
            break
    attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}")
if __name__ == "__main__":
    guess_the_number()