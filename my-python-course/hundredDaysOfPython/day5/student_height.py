students_heights = input("input a list of students heights: \n").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0
for height in students_heights:
    total_height += height
# print(total_height)

number_of_students = 0
for student in students_heights:
    number_of_students += 1
# print(number_of_students)

average_height_of_students = total_height / number_of_students
# print(average_height_of_students)
print(f"The average student height is {round(average_height_of_students)}")
