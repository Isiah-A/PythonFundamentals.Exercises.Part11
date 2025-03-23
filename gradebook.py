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
        self.instructor_id = ("Instructor_" + str(uuid.uuid4()))

class Student(Person):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)
        self.student_id = ("Student_" + str(uuid.uuid4()))

class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class PerK(Student):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class MiddleSchool(Student):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class CollegeStudent(Student):
    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)


