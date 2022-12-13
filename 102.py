list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe_size}
print(list)
user_input = input("Enter a name: ")
print(list [user_input])
#Have no idea why it's not working. Line 7 will show correct array but line 9 print only last record