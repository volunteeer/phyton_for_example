num = int(input("Please a number "))
num2 = int(input("Please a another number "))
total = num + num2
ans = "y"
while ans == "y":
    num3 = int(input("Please a number "))
    total = total + num3
    ans = input("Would you like to add another one? (y/n) ")
print("Summ of all numbers is", total)