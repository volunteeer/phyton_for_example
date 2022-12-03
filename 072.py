subjects = ["Math","Geography","Physics","Byology","English","Chemistry"]
for i in subjects:
    print(i)
user_input = input("Type in one subject you don't like: ")
input_to_indexes = subjects.index(user_input)
del subjects[input_to_indexes]
for i in subjects:
    print(i)
