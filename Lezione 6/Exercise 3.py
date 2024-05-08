class Animal:
    
    def __init__(self, name: str, legs: int,):
        self.name: str = name
        self.legs: int = legs

    
    def setLegs(self,legs: int):
        self.legs = legs
    
    def getLegs(self)-> int:
        return self.legs

    def __str__(self)-> str:
        return f"Nome: {self.name}\nZampe: {self.legs}"

cane = Animal("Cane", 4)
pollo = Animal("Pollo", 2)

pollo.legs = 3

pollo.setLegs(4)

print(cane)
print(pollo)

