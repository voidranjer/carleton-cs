from random import randint

def main():
    # inclusive -> [1, 100], not [1, 100)
    random_int = randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    diff = abs(guess - random_int)
    
    # checks if win/lose, and prints out difference
    if random_int == guess:
        print(f"You won! The number was {random_int}, just like what you guessed!")
    else:
        print(f"Your guess was {guess}, but the number was {random_int}!")
        print(f"You were off by {diff}.")

if __name__ == "__main__":
    main()