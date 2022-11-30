bottles = 5
print("There are", bottles,"green bottles hagning on the wall.")
while bottles > 0:
    print(bottles,"green bottles hagning on the wall,\n and if one bottle should accidentaly fail.")
    b_left = int(input("How many green bottles will be hanging on the wall? "))
    if b_left == bottles - 1:
        bottles = bottles - 1
        print("There will be", bottles, "hagning on the wall")
    else:
        print("No, try again")
print("There are no bottles hanging on the wall")