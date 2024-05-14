class Fence:
    
    def __init__(self, area: float, temperature: float, habitat: str, animals: list[object]) -> None:
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = animals


class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, fence : Fence = None) -> None: # non metto health negli attributi perchè viene calcolato e non passato
        
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)
        self.fence: Fence = fence


class ZooKeeper:

    def __init__(self, name: str, surname: str, id: str) -> None:

        self.name: str = name
        self.surname: str = surname
        self.id: str = id

    def add_animal(animal: Animal, fence: Fence):
        
        #se l'area disponibile della fence è maggiore uguale all'area dell'animele (height*width) agiungi alla fence sottraendo l'area disponibile
        
        if fence.area >= round(animal.height * animal.width, 3):
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width
            animal.fence = fence


    def remove_animal(animal: Animal, fence: Fence):

        fence.animals.remove(animal)

    def feed(animal: Animal):

        if round(animal.height * 2 / 100 * animal.width * 2 / 100, 3) <= animal.fence.area:
            
            # sottrarre l'area occupata dall'area residua
            animal.fence.area = animal.fence.area - round(animal.height * 2 / 100 * animal.width * 2 / 100, 3)

            animal.height = round(animal.height * 102 / 100 , 3)
            animal.width = round(animal.width * 102 / 100 , 3)
            animal.health = round(animal.health * 101 / 100, 3)
           

    def clean(fence: Fence) -> float :
        tempo: float = 0
        area_animals: float = 0

        for i in fence.animals:

            area_animals = area_animals + round(i.height * i.width, 3)

        tempo = round(area_animals / fence.area, 3)

        if fence.area == 0:

            print("L'area residua della fence è pari a 0, restituisco l'area occupata degli animali")
            return area_animals
        else:
            return tempo
        

    

class Zoo:

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers

        
    def describe_zoo(self) -> str:
        
        print("Guardians:")
        for i in self.zoo_keepers:
            print(f"{i.__class__.__name__}(name={i.name}, surname={i.surname} id={i.id})")

        print("Fences:")
        for i in self.fences:
            print(f"{i.__class__.__name__}(area={i.area}, temperature={i.temperature}, habitat={i.habitat})")

            print("with animals")
            for j in i.animals: 
                print(f"{j.__class__.__name__}(name={j.name}, species={j.species}, age={j.age})")
            
            print("#"*30)

gey: ZooKeeper = ZooKeeper("Gey", "Papio", "1234")

a1: Animal = Animal("Pippo", "Pupus", 25, 1.70, 0.6, "Continentale") #mettere il controllo dell'habitat, se è uguale alla fence

f1: Fence = Fence(5, 24, "Continentale",)        


            







