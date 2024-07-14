class User:

    def __init__(self, first_name: str, last_name: str, età: int, genere: str, follower: int, seguiti: int) -> None:

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.età: int = età
        self.genere: str = genere
        self.follower: int = follower
        self.seguiti: int = seguiti


    def describe_user(self) -> None:

        print(f"{self.__class__.__name__}:\n"
        f"First name: {self.first_name}\n"
        f"Last name: {self.last_name}\n"
        f"Età: {self.età}\n"
        f"Genere: {self.genere}\n"
        f"Follower: {self.follower}\n"
        f"Seguiti: {self.seguiti}\n")

    def greet_user(self) -> None:
        print(f"Grazie per aver effettuato l'accesso {self.first_name} {self.last_name}\n")

a: User = User("Geymark Emmanuel","Papio",20,"M",20,20)
b: User = User("Grace Mackenzie","Papio",18,"F",10,10)

a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()
