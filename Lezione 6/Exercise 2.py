class Student:

    def __init__(self,name: str, studyProgram: str, age: int, gender: str):

        self.name: str = name
        self.studyProgram: str = studyProgram
        self.age: int = age
        self.gender: str = gender





    def __str__(self)-> str:
        return f"Nome: {self.name}\nProgramma di studio: {self.studyProgram}\nEtà: {self.age}\nSesso: {self.gender}"
    
Gey = Student("Gey", "Full Stack", 20, "Maschio")
AlessandroVitale = Student("Alessandro Vitale", "Full Stack", 27, "Maschio")
AlessandroSereni = Student("Alessandro Sereni", "Full Stack", 42, "Maschio")

print(Gey)
print()
print(AlessandroVitale)
print()
print(AlessandroSereni)