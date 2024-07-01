class Animal:

    def __init__(self,specie: str, eta: int):

        self.specie: str = specie
        self.eta: int = eta

        def verso():
            pass


class Cat(Animal):

    def __init__(self, specie: str, eta: int, nome: str):
        super().__init__(specie, eta)
        self.nome: str = nome

    def __str__(self) -> str:
        return f"specie: {self.specie} età: {self.eta}/n nome: {self.nome}"


class Rabbit(Animal):
    def __init__(self, specie: str, eta: int, nome: str):
        super().__init__(specie, eta)
        self.nome = nome

class Person(Animal):
    def __init__(self, specie: str, eta: int,nome: str, cognome: str):
        super().__init__(specie, eta)
        self.nome: str = nome
        self.cognome: str = cognome

    def __str__(self) -> str:
        return f"nome: {self.nome} cognome: {self.cognome}\n
                specie: {self.specie}
                età: {self.eta}

                "

class Student(Person):
    def __init__(self, specie: str, eta: int, nome: str, cognome: str, matricola: str):
        super().__init__(specie, eta, nome, cognome)
        self.matricola: str = matricola

    
    


p: Person = Person("Umano",20,"Geymark Emmanuel","Papio")











