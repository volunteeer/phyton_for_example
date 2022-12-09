from array import *

newarray = array('i',[456,103,56,82,11])
for x in newarray:
    print(x)
num = int(input("Enter a number from the list: "))
while num not in newarray:
    print("Slecetd number not in the array")
    for i in newarray:
        print(i)
    num = int(input("Enter a number FROM the list: "))
print(newarray.index(num))

