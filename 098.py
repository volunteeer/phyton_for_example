simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
raw = int(input("Choose a raw: "))
print(simple_array[raw])
user_input = int(input("Enter a number: "))
simple_array[raw].append(user_input)
print(simple_array[raw])