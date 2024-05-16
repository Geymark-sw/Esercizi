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

    def add_animal(self, animal: Animal, fence: Fence):
        
        #se l'area disponibile della fence è maggiore uguale all'area dell'animele (height*width) agiungi alla fence sottraendo l'area disponibile
        
        if isinstance(animal, Animal) and isinstance(fence, Fence):

            if fence.area >= animal.height * animal.width and animal.preferred_habitat.lower() == fence.habitat.lower():
                fence.animals.append(animal)
                fence.area -= animal.height * animal.width
                animal.fence = fence
        else:
            print("Gli oggetti passati non sono del tipo corretto")
            exit(1) #visto che gli oggetti passati sono sbagliati faccio terminare il programma

    def remove_animal(self, animal: Animal, fence: Fence):
        
        if isinstance(animal, Animal) and isinstance(fence, Fence):
            if animal in fence.animals:
                fence.animals.remove(animal)

            else:
                print("L'animale non è presente nel recinto")
        else:
            print("Gli oggetti passati non sono del tipo corretto")

    def feed(self, animal: Animal):

        if isinstance(animal, Animal):

            if ((animal.height * 0.02) * animal.width * 1.02) + ((animal.width * 0.02) * animal.height) <= animal.fence.area:
                
                # sottrarre l'area occupata dall'area residua
                animal.fence.area = animal.fence.area - (((animal.height * 0.02) * animal.width * 1.02) + ((animal.width * 0.02) * animal.height))
                                                    #2% dell'altezza*il totale della base INCREMENTATA    per      2%larghezza*il totale dell'altezza INCREMENTATA               

                animal.height = animal.height * 1.02
                animal.width = animal.width * 1.02
                animal.health = animal.health * 1.01

                #
            else:
                print("L'animale non  può essere nutrito perchè non c'è più spazio")


        else:
            print("L'animale non può essere nutrito perchè non è un oggetto Animale")  

    def clean(self, fence: Fence) -> float :

        if isinstance(fence, Fence):
            tempo: float = 0
            area_animals: float = 0

            for i in fence.animals:

                area_animals = area_animals + i.height * i.width

            if fence.area == 0:

                print("L'area residua della fence è pari a 0, restituisco l'area occupata degli animali")
                return area_animals
            else:

                tempo = area_animals / fence.area
                return tempo
            
        else:
            print("Il recinto non può essere pulito perchè non è un oggetto Recinto")
        

    

class Zoo:

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers

        
    def describe_zoo(self) -> str:
        
        print("Guardians:")
        for i in self.zoo_keepers:
            print(f"{i.__class__.__name__}(name={i.name}, surname={i.surname}, id={i.id})")

        print("Fences:")
        for i in self.fences:
            print(f"{i.__class__.__name__}(area={i.area}, temperature={i.temperature}, habitat={i.habitat})")

            print("with animals")
            for j in i.animals: 
                print(f"{j.__class__.__name__}(name={j.name}, species={j.species}, age={j.age})")
            
            print("#"*30)







            







