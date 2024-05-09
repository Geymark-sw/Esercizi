class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health: float) -> None:
        
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = health

class Fence:
    
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat

class ZooKeeper:

    def __init__(self, name: str, surname: str, id: str) -> None:

        self.name: str = name
        self.surname: str = surname
        self.id: str = id

    def add_animal(animal: Animal, fence: Fence):

        #se l'area disponibile della fence è maggiore uguale all'area dell'animele (height*width) agiungi alla fence sottraendo l'area disponibile
        

class Zoo:

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers





