from array import *
import random
array1 = array('i',[])
array2 = array('i',[])
for a in range(0,5):
    num = random.randint(0,1000)
    array1.append(num)
for i in range(0,3):
    num = int(input("Enter a number: "))
    array2.append(num)
array1.extend(array2)
totalarray = sorted(array1)
for x in totalarray:
    print(x)