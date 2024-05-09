"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods."""

class Restaurant:

    def __init__(self, name: str, cucine_type: str):

        self.name: str = name
        self.cucine_type: str = name


    def describe_restaurant(self):

        print(f"Restaurant(Name: {self.name},
              cuisine: {self.cucine_type})")
        
    def open_restaurant(self):
        print(f"Il ristortante {self.name} è aperto")

r1: Restaurant = Restaurant("Burger King", "Fast food")
r1.describe_restaurant()
r1.restaurant()
print("#" * 30)
r2: Restaurant = Restaurant("Burger King", "Fast food")
r2.describe_restaurant()
r2.restaurant()
        


