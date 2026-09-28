
from Student import Student, UndergraduateStudent, GraduateStudent




student1 = Student(
    "Karim",
    "CSE001",
    "karim@gmail.com",
    22,
    "CSE"
)




student2 = UndergraduateStudent(
    "Ahsan",
    "CSE101",
    "ahsan@gmail.com",
    23,
    "CSE",
    8
)


student3 = GraduateStudent(
    "Rahim",
    "CSE201",
    "rahim@gmail.com",
    25,
    "CSE",
    "Artificial Intelligence"
)


student2.add_marks(80, 85, 90)
student3.add_marks(75, 80, 85)


print("===== STUDENT 1 =====")

student1.display_info()

print("Student Type:", student1.get_student_type())
print("Result:", student1.calculate_result())


print()


print("===== STUDENT 2 =====")

student2.display_info()

print("Semester:", student2.semester)
print("Student Type:", student2.get_student_type())
print("Result:", student2.calculate_result())


print()


print("===== STUDENT 3 =====")

student3.display_info()

print("Research Topic:", student3.research_topic)
print("Student Type:", student3.get_student_type())
print("Result:", student3.calculate_result())


print()
print("===== METHOD OVERRIDING =====")

print("Student:", student1.get_student_type())
print("Undergraduate:", student2.get_student_type())
print("Graduate:", student3.get_student_type())



print()
print("===== METHOD OVERLOADING =====")


student2.add_marks(95)

print("After adding 1 mark student(2):", student2.get_marks())



student2.add_marks(88, 92)

print("After adding 2 marks student(2):", student2.get_marks())




print()
print("===== POLYMORPHISM =====")

students = [student1, student2, student3]

for student in students:
    print(student.get_student_type())

