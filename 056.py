import random
numtoguess = random.randint(1,10)
guess = int(input("Guess a number in range 1 to 10: "))
while guess != numtoguess:
    print("Wrong!")
    guess = int(input("Guess again: "))
print("Well done")