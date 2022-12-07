from array import *
array1 = array('i',[])
for i in range (0,5):
    num = int(input("Enter a number: "))
    array1.append(num)
newarray = sorted(array1)
for a in newarray:
    print(a)
exclude = int(input("Choose a number from array: "))
if exclude in array1:
    newarray.remove(exclude)
    array2 = array('i',[])
    array2.append(newarray)
    print(newarray)
    print(array2)
else:
    print("Not in array!")