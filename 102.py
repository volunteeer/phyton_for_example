list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = input("Enter age: ")
    shoe_size = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe_size}
print(list)
user_input = input("Enter a name: ")
print(list [name])
#Have no idea why it's not working. Line 7 will show correst array but line 9 print only last record