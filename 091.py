from array import *
newarray = array('i',[45,14,64,14,66])
for x in newarray:
    print(x)
userinput = int(input("Enter a number form an array: "))
print(newarray.count(userinput))
