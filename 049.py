compnum = 50
guess = int(input("Can you guess a number?: "))
attempt = 0
while guess != compnum:
    if guess < compnum :
        print("Your number is too low")
        
    else:
        print("Your number is too high")
    attempt = attempt + 1
    guess = int(input("Please enter a number: "))
print("Well done!, you took", attempt,"attempts")