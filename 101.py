data_set = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},"Anna":{"N":5239,"S":4802,"E":5820,"W":1859},"Flona":{"N":3904,"S":3645,"E":8821,"W":2451}}
name = input("Enter a name: ")
region = input("Enter a region: ")
print(data_set[name] [region])
user_input = input("Would you like to chane this value? (y/n): ")
if user_input == "y":
    new_value = int(input("Enter value: "))
    data_set [name] [region] = new_value
    print(data_set[name])