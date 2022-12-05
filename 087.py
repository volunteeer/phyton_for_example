word = input("Enter a word: ")
letter_total = len(word)
num = 1
for i in word:
    pos = letter_total - num
    cur_letter = word[pos]
    print(cur_letter)
    num = num + 1