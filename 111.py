import csv
record1 = "To Kill a Mockingbird, Harper Lee, 1960\n"
record2 = "A Brief History of Time, Stephen Hawking, 1988\n"
record3 = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
record4 = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
record5 = "Pride and Prejudice, Jan Austen, 1813\n"
file = open("Books.csv", "w")
file.write(str(record1))
file.write(str(record2))
file.write(str(record3))
file.write(str(record4))
file.write(str(record5))
file.close()