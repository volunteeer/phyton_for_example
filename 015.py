from socket import RDS_CANCEL_SENT_TO


text = input("Please type your favorite collour\n")
if text == "red" or text == "RED" or text == "Red":
    print("I like red too!")
else:
    print("I don't like",text,"I prefer red")