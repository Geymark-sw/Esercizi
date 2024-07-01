class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobby: list[str] = set()

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

    def remove_hobby(self, hobby):
        self.hobby.remove(hobby)

    def __str__(self) -> str:
        return(f"Nome: {self.name}, età: {self.age}")

alice = Person("Alice W.", 45)
bob = Person("Bob", 36)

#1
print(bob.age)

#2
if bob.age > alice.age:
    print(bob.age)

else:
    print(alice.age)

#3
pippo = Person("Pippo", 20)
pluto = Person("Pluto", 21)
paperino = Person("Paperino", 21)




