list = {}
for i in range(0,4):
    name = input("Enter name: ")
    age = input("Enter age: ")
    shoe_size = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe_size}
for i in list:
    print((i), list[name] ["Age"])