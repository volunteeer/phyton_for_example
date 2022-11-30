import random
side = random.choice(["h","t"])
guess = input("Enter (h)eads or (t)ails ")
if guess == side:
    print("You win!")
else:
    print("Bad luck")
if side == "h":
    print("It was head")
else:
    print("It was tail")