import random

QUIZ_NUMBER = 10
count = 0
correct_answers = 0
wrong_answers = 0

shape = "*"
print(shape * 17)
print("****MATH QUIZ****")
print(shape * 17)

while count < QUIZ_NUMBER:

    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)

    user_answer = eval(input(f"{count + 1}. {number1} + {number2} = "))
    result = number1 + number2
    count += 1

    if user_answer == result:
        print(">>>Correct")
        correct_answers += 1
    else:
        print(">>>Wrong")
        wrong_answers += 1

print()
print("You got ", correct_answers, "questions correctly")
print("You failed ", wrong_answers, "questions")

total_score = correct_answers - wrong_answers
print("You total score is ", total_score)
