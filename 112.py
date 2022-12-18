import csv

title = input("Enter a title of a new Book: ")
author = input("Enter the name of the Author: ")
year = input("Enter a name it was released: ")
file = open("Books.csv", "a")
file.write(title + ", " + author + ", " + year + "\n")
file.close()
file = open("Books.csv")
for i in file:
    print(i)