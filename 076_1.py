#little upgrade of 076. Didn't read exersise well at the beginning
# For my opinion it's the better solution for this exercise
guests_list = {}
number_of_guests = 1
guest = input("Whom you would like to invite on the pary: ")
guests_list[number_of_guests] = guest
question = input("Would you like to invite someone else? (y/n) ")
while question == "y":
    number_of_guests = number_of_guests + 1
    guest = input("Whom else you would like to invite on the pary: ")
    guests_list[number_of_guests] = guest
    question = input("Would you like to invite someone else? (y/n) ")
print(number_of_guests)
print(guests_list)

