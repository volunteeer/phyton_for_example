nums = []
num1 = int(input("Enter a number: "))
nums.append(num1)
num2 = int(input("Enter a number: "))
nums.append(num2)
num3 = int(input("Enter another number: "))
nums.append(num3)
question = input("Would you like to save last number? (yes/no) " )
if question == "no":
    nums.remove(num3)
print(nums)