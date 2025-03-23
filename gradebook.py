import enum
import uuid


class AliveStatus(enum.Enum):
    deceased = 0
    alive = 1

class Person:
    def __init__(self, first_name, last_name, dob, AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus.alive

    def update_first_name(self, name):
        self.first_name = name

    def update_last_name(self, name):
        self.last_name = name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, status):
        self.alive = status

class Instructor(Person):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)
        self.instructor_id = "Instructor_" + str(uuid.uuid4())

class Student(Person):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)
        self.student_id = "Student_" + str(uuid.uuid4())

class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class PerK(Student):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)


class Classroom:
    def __init__(self):
        self.students: dict[int, Student] = dict()
        self.instructors : dict[Instructor.instructor_id, Instructor] = dict()


    def add_instructor(self, instructor:Instructor):
        self.instructors[instructor.instructor_id] = instructor


    def remove_instructor(self, instructor:Person):
        self.instructors = {y: x for y, x in self.instructors.items() if x != instructor}


    def add_student(self, student:Student):
        self.students[student.student_id] = student

    def remove_student(self, student:Person):
        self.students = {y: x for y, x in self.students.items() if x != student}

    def print_instructors(self):
        [print(f"{key}: {value}") for key, value in self.instructors.items()]

    def print_students(self):
        [print(f"{key}: {value}") for key, value in self.students.items()]


bob = Person('bob', 'johnson', 12 / 12 / 2000, AliveStatus.alive)
bob_student = Student('bob', 'johnson', 12/12/2000, AliveStatus.alive) #shouldn't have to add same fields??
room12 = Classroom()
room12.add_student(bob_student)
room12.print_students()
room12.remove_student(bob_student)

