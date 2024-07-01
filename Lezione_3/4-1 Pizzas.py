"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, 
    you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, 
    outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
    such as I really love pizza!
"""

def stampa_pizza(pizza: list) -> str:

    for i in pizza:

        if i.lower() == "margherita":

            print(f"Mi piace la pizza {i.lower()}, amo il sugo e la mozzarella")

        elif i.lower() == "boscaiola":

            print(f"Mi piace la pizza alla {i.lower()} perchè ci sta la salsiccia")
        
        elif i.lower() == "diavola":

            print(f"Mi piace la pizza alla {i.lower()} perchè amo il salame")

    return"Amo la pizza"

pizza: list[str] = ["margherItA","BoscAiola","diavOla"]

print(stampa_pizza(pizza))

