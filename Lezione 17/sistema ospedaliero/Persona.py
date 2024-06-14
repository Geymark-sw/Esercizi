class Persona:

    def __init__(self, _first_name: str, _last_name: str) -> None:
        
        if type(_first_name) == "str":

            self._first_name: str = _first_name
        else:
            print("Il nome non è una stringa")
            self._first_name: str = None

        if type(_last_name) == "str":

            self._last_name:str = _last_name
        else:
            print("Il cognome non è una stringa")
            self._last_name:str = None

        if isinstance(_first_name,str) and isinstance(_last_name,str):

            self.age: int = 0

        else:

            self.age: int = None


    def set_first_name(self,_first_name: str):

        if isinstance(_first_name, str):
            self._first_name = _first_name

        else:
            print("Il nome inserito non è una stringa") 

    def set_last_name(self,_last_name: str):

        if isinstance(_last_name, str):
            self._last_name = _last_name

        else:
            print("Il cognome inserito non è una stringa")

    def set_age(self, age: int):

        if isinstance(age, int):
            self.age = age

        else:
            print("L'età inserita non è un intero")

    def get_first_name(self):

        return self._first_name

    def get_last_name(self):

        return self._last_name

    def greet(self):

        print(f"Ciao, sono {self._first_name} {self._last_name}! Ho {self.age} anni") 

        
              

