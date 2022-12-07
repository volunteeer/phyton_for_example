from array import *
newarry = array('i',[])
count = 1
while count < 6:
    num = int(input("Enter a number betwwen 10 and 20: "))
    if num >= 10 and num <=20:
        newarry.append(num)
        count = count + 1
        print("Saved!")
    else:
        print("Out of range")
print("Thank you!")
for x in newarry:
    print(x)