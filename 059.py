import random
collour  = random.choice(["green","black","yellow","red","magenta"])
answer = input("Guess a collour: ")
while collour != answer:
    print("Tip:",collour[0:3])
    answer = input("Guess collour again: ")
print("Correct! The collour is",collour)