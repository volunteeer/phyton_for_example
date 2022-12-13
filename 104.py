list = {}
for i in range(0,2):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    list[name] = {"Age":age, "Shoe size":shoe_size}
correction = input("Whom you would like to remove from the list?: ")
del list[correction]
for name in list:
    print((name), list[name]["age"], list[name]["Shoe size"] )
# This one needed to be fixed. Code in the book is not correct. Will come abck to this latter after getting more skills