num = int(input("How many pepople you would like to invite on a party? "))
if num >=10:
    print("To many people!")
else:
    for i in range(1,num+1):
        name = input("Enter a name of guest: ")
        print(name, "has been invited")