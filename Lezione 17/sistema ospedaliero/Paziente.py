from Persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, codice_identificativo: str) -> None:
        super().__init__(first_name, last_name)
        self.__codice_identificativo: str = codice_identificativo

    def set_codice_identificativo(self, codice_identificativo: str):

        self.__codice_identificativo = codice_identificativo

    def get_codice_identificativo(self):
        return self.__codice_identificativo
    
    def patient_info(self):
        print(f"{self.__class__.__name__}: {self.__first_name} {self.__last_name} \n"
              f"ID: {self.get_codice_identificativo()}")
        
        