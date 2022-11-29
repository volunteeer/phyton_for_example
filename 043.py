count = input("Do you whant count up or down? ")
if count == "up":
    num = int(input("Please enter a number: "))
    for i in range(1,num+1, 1):
        print(i)
if count == "down":
    num = int(input("Please enter a number below 20: "))
    if num >20:
        print("I don't understand")
    for g in range(20, num-1, -1):
        print(g)