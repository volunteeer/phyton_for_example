from array import  *
import random
newarry = array('i',[])
for i in range(0,5):
    num = random.randint(0,10000)
    newarry.append(num)
for x in newarry:
    print(x)
