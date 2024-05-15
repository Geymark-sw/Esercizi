from ITS.people.person import Person


class Lecturer(Person):
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)