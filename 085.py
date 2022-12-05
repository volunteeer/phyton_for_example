name = input("Enter your name: ")
vowels_count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels_count = vowels_count + 1
print(vowels_count,"vowels in your name")