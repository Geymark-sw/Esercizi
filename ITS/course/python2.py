from group import Group
from people.student import Student
from abc import ABC, abstractmethod
class CourseAB(ABC):

    def __init__(self, name) -> None:
        super().__init__()

        self.name: str = name
        self.groups: list[Group] = []

    def register_student(self, student: Student):
            pass

    def add_group(self, group: Group):
        
        
        self.groups.append(group)