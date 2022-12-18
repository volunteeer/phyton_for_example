selector = int(input("1) Create a new file\n2) Display the file\n3) Add new item to the file\n"))
if selector == 1:
    subj = input("Enter a school subject name: ")
    file = open("Subject.txt", "w")
    file.write(subj + "\n")
    file.close()
elif selector == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close
elif selector == 3:
    file = open("Subject.txt", "a")
    new_subject = input("Enter new subject: ")
    file.write(new_subject + "\n")
    file.close()
else:
    print("Error")