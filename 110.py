file = open("Name.txt", "r")
print(file.read())
file.close()

file = open("Name.txt", "r")
select_name = input("Choose the name from the list: ")
select_name = select_name + "\n"
for i in file:
    if i != select_name:
        file = open("Names2.txt", "a")
        record = i
        file.write(i)
        file.close()
file.close()