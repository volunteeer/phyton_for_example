import random
correct_answer = 0
num_sentence = 0
while num_sentence < 5:
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    answer = num1 + num2
    print("Count the sentence: ",num1,"+",num2,"= ")
    user_answer = int(input("Your answer: "))
    if user_answer == answer:
        correct_answer = correct_answer + 1
    num_sentence = num_sentence + 1
print("You have",correct_answer,"correct answers")
