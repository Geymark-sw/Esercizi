pizza: list[str] = ["margherItA","BoscAiola","diavOla"]

friend_pizzas: list[str] = ["margherItA","BoscAiola","diavOla"]

pizza.append("capricciosa")

friend_pizzas.append("carbonara")

print(f"Le mie pizze preferite sono:")

for i in pizza:

    print(i)


print(f"Le pizze preferite del mio amico sono:")

for i in friend_pizzas:

    print(i)
