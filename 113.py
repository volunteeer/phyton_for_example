import csv

bookstoadd = int(0)
numberofbooks = int(input("How many new books you would like to add? "))
while bookstoadd < numberofbooks:
    file = open("Books.csv", "a")
    title = input("Enter a title of a new Book: ")
    author = input("Enter the name of the Author: ")
    year = input("Enter a name it was released: ")
    file = open("Books.csv", "a")
    file.write(title + ", " + author + ", " + year + "\n")
    bookstoadd = bookstoadd + 1
    file.close()

search = input("Enter the name of author you are looking for: ")
file = open("Books.csv", "r")
booksinlist = 0
for i in file:
    if search in str(i):
        print(i)
        booksinlist = booksinlist + 1
if booksinlist == 0:
    print("There is no author " + search + " in the list")
file.close()