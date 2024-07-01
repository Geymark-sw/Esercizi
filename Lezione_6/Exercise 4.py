class Food:

    def __init__(self, name: str, price: float, description: str = None):

        self.name = name
        self.price = price
        self.description = description


class Menu:

    def __init__(self, foods: list[Food] = []):

        self.foods = foods


    def addFood(self, food: Food):

        self.foods.append(food)

    def removeFood(self, food: Food):

        self.foods.remove(food)

    def __str__(self) -> str:

        stri: str = ""

        for food in self.foods:
            stri += food.__str__ +"\n"



        return f"Menu: {self.foods}"

    
    


carbonara = Food("Carbonara",7.5)
margherita = Food("Margherita", 6.5)
boscaiola = Food("Boscaiola", 7)
lasagna = Food("Lasagna", 7)

lista_di_cibo :list[Food] = [carbonara,margherita,boscaiola]

menu = Menu(lista_di_cibo)

menu.addFood(lasagna)
menu.removeFood(boscaiola)
print(menu)