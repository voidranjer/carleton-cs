import random

ans = random.randint(1, 100)
response = int(input("Guess a number: "))

while True:
    if response > ans:
        print("Guess lower")
    elif response < ans:
        print("Guess higher")
    response = int(input("Guess a number: "))
    if response == ans:
        print("Congratulations! You won!")
        break