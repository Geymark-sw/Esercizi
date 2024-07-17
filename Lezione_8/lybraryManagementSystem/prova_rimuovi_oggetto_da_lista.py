class Oggetto:

    def __init__(self,id: int, valore: str):

        self.id: int = id
        self.valore: str = valore


    def __eq__(self,value: object):

        if isinstance(value,Oggetto):

            return self.id == value.id
        return False
    
o1: Oggetto = Oggetto(123,"ciao")
o2: Oggetto = Oggetto(456,"ciao")
o3: Oggetto = Oggetto(678,"a tutti ragazzi")

lista_oggetti: list[Oggetto] = [o1,o2,o3]

print(lista_oggetti)

print(o1 == o2)

lista_oggetti.remove(o1)

print(lista_oggetti)

