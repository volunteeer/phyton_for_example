name1 = input("Enter an name of a guest you would like to invite on the party: ")
name2 = input("Whom else you would like to invite?: ")
name3 = input("Whom else you would like to invite?: ")
party_list = [name1,name2,name3]
question = input("would you like to invite someone else?: (yes/no)")
while question == "yes":
    name_add = party_list.append(input("Enter another name: "))
    question = input("would you like to invite someone else?: (yes/no)")
print("You have", len(party_list),"guest invited on your party")

