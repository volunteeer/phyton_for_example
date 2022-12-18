file = open("Name.txt", "a")
new_name = input("Eneter a new name: ")
file.write(new_name + "\n")
file.close()

file = open("Name.txt", "r")
print(file.read())
file.close()