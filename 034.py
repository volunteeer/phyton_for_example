print("1) Square\n"
        "2) Triangle")
selection = int(input("Input 1 or 2\n"))
if selection == 1:
    side = int(input("Enter the lengh of a side\n"))
    print("The area of the shape will be",side**2)
elif selection == 2:
    base = int(input("Enter the lengh of a side\n"))
    hight = int(input("Enter the hight of the triangele\n"))
    print("The area of the shape will be",int((base*hight)/2))
else:
    print("Error! enter 1 or 2")