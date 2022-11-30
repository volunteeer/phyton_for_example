from operator import inv


invite = "y"
numberofguests = 0
while invite == "y":
    input("Enter a name of a guest: ")
    numberofguests = numberofguests + 1
    invite = input("Would you like to invite someone else? (y/n): ")
print("Total guests:", numberofguests)
