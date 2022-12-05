word = (input("Enter a word in upper case: "))
case = False
while case == False:
    if word.isupper():
        print("Thanks!")
        case = True
    else:
        word = (input("Enter a word in upper case: "))