#find the second lowest total marks of any student(s) from the given names and marks of each student

num = int(input("Enter number of students: "))
students = []

for i in range(num):
    name = input("Enter name of student:")
    marks = int(input("Enter marks of student:"))
    students.append([name,marks])

sorted_students = sorted(students, key= lambda x: int(x[1])) #sort wrt marks(which is the 2nd attr in nested list)
print(sorted_students)

for i in range(len(sorted_students)):
    if sorted_students[0][1] != sorted_students[i][1]: #checks konse inner list ka marks wala attribute is not equal to the lowest(first inner list) ke marks
        print("student with seond lowest marks is: ",sorted_students[i])
        break