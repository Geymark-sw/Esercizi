class User:

    def __init__(self, first_name: str, last_name: str, età: int, genere: str, follower: int, seguiti: int) -> None:

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.età: int = età
        self.genere: str = genere
        self.follower: int = follower
        self.seguiti: int = seguiti


    def describe_user(self) -> str:

        print(f"{self.__class__.__name__}\n"
        f"First name: {self.first_name} L")


a: User = User("Geymark Emmanuel","Papio",20,"M",20,20)

a.describe_user()