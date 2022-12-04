numbers_list = [453,843,711,666]
for i in numbers_list:
    print(i)
user_input = int(input("Please enter a three digit number: "))
if user_input in numbers_list:
    number_index = numbers_list.index(user_input)
    print("position of the number in the list is:",number_index)
else:
    print("Number is not in the list")