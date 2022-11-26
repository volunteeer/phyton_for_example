from tkinter.messagebox import YES


text = input("Is it reiny?\n")
text = str.lower(text)
if text == "yes":
    text2 = input("Is it windy today?\n")
    text2 = str.lower(text2)
    if text2 == "yes":
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella!")
else:
    print("Have a good day!")