class Persona:

    def __init__(self, first_name: str, last_name: str) -> None:
        
        if type(first_name) == "str":

            self.__first_name: str = first_name
        else:
            print("Il nome non è una stringa")
            self.__first_name: str = None

        if type(last_name) == "str":

            self.__last_name:str = last_name
        else:
            print("Il cognome non è una stringa")
            self.__last_name:str = None

        if isinstance(first_name,str) and isinstance(last_name,str):

            self.__age: int = 0

        else:

            self.__age: int = None


    def set_first_name(self,first_name: str):

        if isinstance(first_name, str):
            self.__first_name = first_name

        else:
            print("Il nome inserito non è una stringa") 

    def set_last_name(self,last_name: str):

        if isinstance(last_name, str):
            self.__last_name = last_name

        else:
            print("Il cognome inserito non è una stringa")

    def set_age(self, age: int):

        if isinstance(age, int):
            self.__age = age

        else:
            print("L'età inserita non è un intero")

    def get_first_name(self):

        return self.__first_name

    def get_last_name(self):

        return self.__last_name

    def greet(self):

        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni") 


              

