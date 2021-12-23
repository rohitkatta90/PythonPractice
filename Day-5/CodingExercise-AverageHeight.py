# Coding Exercise - Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student scores ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Approach-1
# numberOfStudents = len(student_heights)
# total_height = sum(student_heights)
# average_height =round(total_height/numberOfStudents)
# print(average_height)

#Approach-2 Using for loop

total_height=0
for height in student_heights:
    total_height = total_height+height
print(total_height)

total_number_of_students = 0
for student in student_heights:
    total_number_of_students=total_number_of_students+1
print(total_number_of_students)

average_height = round(total_height / total_number_of_students)
print(average_height)
