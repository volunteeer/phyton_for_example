total = 0
for i in range(1,6):
    num = int(input("Please enter a number: "))
    ans = input("Do you want this number to be included? Yes or No: ")
    if ans == "Yes":
        total = total + num
print(total)