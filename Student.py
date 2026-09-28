class Student:

    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        self.__marks = []

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Email:", self.__email)
        print("Age:", self.age)
        print("Department:", self.department)

    def calculate_result(self):
        if len(self.__marks) == 0:
            return "No marks available"

        average = sum(self.__marks) / len(self.__marks)

        if average >= 80:
            return "A+"
        elif average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"

    def get_student_type(self):
        return "Student"


    def add_marks(self, *marks):
        self.__marks.extend(marks)


    def get_marks(self):
        return self.__marks


class UndergraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department
        )

        self.semester = semester


    def get_student_type(self):
        return "Undergraduate Student"


class GraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department
        )

        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"