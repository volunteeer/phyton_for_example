from array import *
import math

newarray = array('f',[10.54,66.22,15.16,49.71,15.99])

inrange = True
while inrange == True:
    userinput = int(input("Enter a number in range 2 to 5: "))
    if userinput < 2 or userinput >5:
        print("Choosen number in not in range!")
    else:
        inrange = False
for i in newarray:
    ans = i / userinput
    print(round(ans,2))

