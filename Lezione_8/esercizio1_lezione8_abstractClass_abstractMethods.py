from abc import ABC,abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Circle(Shape):

    def area(self, r: float) -> float:

        return math.pi * r**2
    
    def perimeter(self, r: float) -> float:

        return 2*math.pi * r
    

class Rectangle(Shape):

    def area(self, base: float, altezza: float) -> float:

        return base * altezza
    
    def perimeter(self, base: float, altezza: float) -> float:

        return base * 2 + altezza * 2
    



c: Circle = Circle()
r: Rectangle = Rectangle()

print(c.area(4))
print(c.perimeter(4))

print(r.area(6,4))
print(r.perimeter(6,4))



