word = input("Please enter a word\n")
check = word[0]
lengh = len(word)
if check != "a" and check != "e" and check != "i" and check != "o" and check != "u" and check != "y":
    print(word[1:lengh] + word[0]+"ay")
else:
    print(word.lower() + "way")