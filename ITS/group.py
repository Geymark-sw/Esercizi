from ITS.people.lecturer import Lecturer
from ITS.people.student import Student


class Group:
    
    def __init__(self, name: str, limit: int):
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []
        
    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> int:
        return self.limit
    
    def get_students(self) -> list[Student]:
        return self.students
    
    def get_limit_lecturers(self):
        return max(len(self.students) // 10, 1)
    
    def add_student(self, student: Student) -> bool:
        limit: int = self.get_limit()
        if student and isinstance(student, Student)\
            and student not in self.students and limit > 0:
            self.students.append(student)
            student.set_group(self)
            self.limit -= 1
            return True
        return False
            
    def add_lecturer(self, lecturer: Lecturer):
        if lecturer and isinstance(lecturer, Lecturer)\
            and lecturer not in self.lecturers and self.get_limit_lecturers() > len(self.lecturers):
                self.lecturers.append(lecturer)