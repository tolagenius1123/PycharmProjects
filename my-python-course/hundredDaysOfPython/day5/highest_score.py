# students_scores = input("Enter student scores: ").split()
# for n in range(0, len(students_scores)):
#     students_scores[n] = int(students_scores[n])
# print(students_scores)
#
# max_score = 0
# for score in students_scores:
#     if score > max_score:
#         max_score = score
#
# min_score = students_scores[0]
# for score in students_scores:
#     if score < min_score:
#         min_score = score
# print(f"The highest student score is {max_score} \n"
#       f"The lowest student score is {min_score}")

total = 0
for num in range(2, 101, 2):
    # print(num, end=" ")
    total += num
print(total)
