food_list = {}
food1 = input("Enter dish you like: ")
food_list[1] = food1
food2 = input("Enter another dish you like: ")
food_list[2] = food2
food3 = input("Enter another dish you like: ")
food_list[3] = food3
food4 = input("Enter another dish you like: ")
food_list[4] = food4
food5 = input("Enter another dish you like: ")
food_list[5] = food5
print(food_list)
remove_food = int(input("Enter the number food you would like to remove from list: "))
del food_list[remove_food]
print(food_list.values())
#this exercise is a holly crap! Output is just...