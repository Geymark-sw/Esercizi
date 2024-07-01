from Persona import Persona


class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)

        if isinstance(specialization, str):

            self.__specialization: str = specialization
        else:
            self.__specialization: str = None
            print("La specializzazione inserita non  è una stringa.")

        if isinstance(parcel, float):

            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcel inserita non è un float")

    
    def set_specialization(self, specialization: str):

        if isinstance(specialization, str):

            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è un stringa.")

    def set_parcel(self, parcel: float):

        if isinstance(parcel, float):

            self.__parcel = parcel
        else:
            print("La parcel inserita non è un float")

    def get_specialization(self):

        return self.__specialization
    
    def get_parcel(self):
        return self.__parcel
    
    def is_a_valid_doctor(self):
        if self.__age > 30:
            print(f"Doctor {self.__first_name} {self.__last_name} is valid!")
            return True
        else:
            print(f"Doctor {self.__first_name} {self.__last_name} is not valid!")
            return False

    def doctor_greet(self):
        super().greet()
        print(f"Sono un medico {self.__specialization}")

    



    
        

        