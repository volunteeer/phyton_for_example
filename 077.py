name1 = input("Enter an name of a guest you would like to invite on the party: ")
name2 = input("Whom else you would like to invite?: ")
name3 = input("Whom else you would like to invite?: ")
party_list = [name1,name2,name3]
question = input("Would you like to invite someone else?: (yes/no) ")
while question == "yes":
    name_add = party_list.append(input("Enter another name: "))
    question = input("Would you like to invite someone else? (yes/no) ")
print("This people are your guests:")
for i in party_list:
    print(i)
choosen_name = input("Please enter one of the names: ")
print("It's number", party_list.index(choosen_name),"in the list")
question2 = input("Would you like this person be on the party? (yes/no) ")
if question2 == "no":
    del party_list[party_list.index(choosen_name)]
print("This people are your guests:")
for i in party_list:
    print(i)