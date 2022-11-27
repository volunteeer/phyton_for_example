name = input("Please enter your name\n")
if len(name) <=5 :
    surname = input("Please enter your surname\n")
    print(name.upper()+surname.upper())
else:
    print(name.lower())