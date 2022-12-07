from array import *
newarray = array('i',[])
count = 1
while count < 6:
    num = int(input("Enter a number: "))
    newarray.append(num)
    count  = count + 1
print(newarray)