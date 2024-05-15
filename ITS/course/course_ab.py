from ITS.group import Group
from ITS.people.student import Student


class Course:
    
    def __init__(self, name: str):
        self.name: str = name
        self.groups: list[Group] = []
        
    def register(self, student: Student):
        for group in self.get_groups():
            if group.add_student(student):
                break
        
    def get_groups(self) -> list[Group]:
        return self.groups
        
    def add_group(self, group: Group):
        if group and isinstance(group, Group)\
            and group not in self.groups:
            self.groups.append(group)