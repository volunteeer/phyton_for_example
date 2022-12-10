simple_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
raw = int(input("Choose a raw: "))
print(simple_array[raw])
col = int(input("Choose a collumn: "))
print(simple_array[raw] [col])
user_ans = input("Do you whant to change the value? (y/n) ")
if user_ans == "y":
    value = int(input("Enter a new value: "))
    simple_array [raw] [col] = value
    print(simple_array[raw])