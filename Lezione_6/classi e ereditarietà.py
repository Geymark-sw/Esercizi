class Persona:

    def __init__(self, name: str, cognome: str, data_di_nascita, genere: str, codice_fiscale) -> None:
        
        self.name: str = name
        self.cognome: str = cognome
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere
        self.codice_fiscale: str = codice_fiscale

    
    def calcola_eta(self) -> int:
        
        return 10
    
    def __eq__(self, value: object) -> bool:
        
        return value.codice_fiscale == self.codice_fiscale


class Dipendente(Persona):

    def __init__(self, name: str, cognome: str, data_di_nascita, genere: str, ore_lavorate) -> None:
        super().__init__(name, cognome, data_di_nascita, genere)

        self.ore_lavorate: int = ore_lavorate

    def calcola_stipendio(self) -> float:

        return 500.0
    
    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)
    
class Professore(Dipendente):

    def __init__(self, name: str, cognome: str, data_di_nascita, genere: str, ore_lavorate, materia_insegnata: str, ore_di_lezione: int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)

        self.materia_insegnata = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione


    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)  



persona_1: Persona = Persona("Gey", "Papio", "25/12/03","Maschio","Ciao")

dipendente_1: Dipendente = Dipendente("Gey", "Papio", "25/12/03","Maschio",500)

professiore_1: Professore = Professore("Gey", "Papio", "25/12/03","Maschio",500, "Python")



print(persona_1.calcola_eta())
print(dipendente_1.calcola_eta())
print(dipendente_1.calcola_stipendio())
print(dipendente_1.ore_lavorate)

