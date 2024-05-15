class Person:
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age
        
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(cf={self.cf}, name={self.name}, surname={self.surname}, age={self.age})'