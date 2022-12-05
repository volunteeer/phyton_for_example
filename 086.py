pass1 = input("Please enter your password: ")
pass2 = input("Please enter your password again: ")
if pass1 == pass2:
    print("Thank you!")
elif pass1.lower() == pass2.lower():
    print("They must be in the same case")
else:
    print("Incorrect!")