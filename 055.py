import random
numtoguess = random.randint(1,5)
guess = int(input("Guess a number in range 1 to 5: "))
if guess == numtoguess:
    print("Well done!")
elif guess < numtoguess:
    guess = int(input("Your guess to low. Try again: "))
    if guess == numtoguess:
        print("Well done!")
    else:
        print("You loose")
elif guess > numtoguess:
    guess = int(input("Your guess to high. Try again: "))
    if guess == numtoguess:
        print("Well done!")
    else:
        print("You loose")