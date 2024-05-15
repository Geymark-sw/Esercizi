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
        
        if fence.area >= animal.height * animal.width and animal.preferred_habitat.lower() == fence.habitat.lower():
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width
            animal.fence = fence


    def remove_animal(self, animal: Animal, fence: Fence):

        fence.animals.remove(animal)

    def feed(self, animal: Animal):

        if animal.height * 2 / 100 * animal.width * 2 / 100 <= animal.fence.area:
            
            # sottrarre l'area occupata dall'area residua
            animal.fence.area = animal.fence.area - animal.height * 2 / 100 * animal.width * 2 / 100
                                                    #2% dell'altezza     per      2%larghezza                

            animal.height = animal.height * 102 / 100
            animal.width = animal.width * 102 / 100
            animal.health = animal.health * 101 / 100

            #
        else:
            print("L'animale non  può essere nutrito perchè non c'è più spazio")
           

    def clean(self, fence: Fence) -> float :
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

zlist: list[ZooKeeper] = [gey]

a1: Animal = Animal("Pippo", "Pupus", 25, 3, 3, "Continentale") #mettere il controllo dell'habitat, se è uguale alla fence
a2: Animal = Animal("Topolino", "Tepus", 18, 3, 1.5, "Artico")
a3: Animal = Animal("Paperino", "Paperninus", 25, 1.1, 1.1, "Continentale")

f1: Fence = Fence(18, 24, "Continentale",[])

flist: list[Fence] = [f1]
print(f1.area)
gey.add_animal(a1, f1)  #add
print(f1.area)
gey.add_animal(a2, f1)
print(f1.area)
gey.add_animal(a3, f1)
print(f1.area)


for i in range(5**2):
    
    gey.feed(a1) #feed
    print(round(gey.clean(f1),3))

    """print(f"Area animale: {round(a1.height*a1.width,3)}")
    print(f"Salute animale: {round(a1.health,3)}")
    print(f"Area fence dentro animal: {round(a1.fence.area,3)}")
    print(f"Area fence oggetto: {round(f1.area,3)}")"""



z1: Zoo = Zoo(flist, zlist)




z1.describe_zoo()
gey.remove_animal(a3, f1)
z1.describe_zoo()




# programma scritto
# controlla funzione feed e altre funzioni






            







