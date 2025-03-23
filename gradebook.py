import enum


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


