def stampa_pizza(animals: list) -> str:

    for i in animals:

        if i.lower() == "dog":

            print(f"I like {i.lower()}s, because they are cool")

        elif i.lower() == "cat":

            print(f"I like {i.lower()}, because they are cute")
        
        elif i.lower() == "cow":

            print(f"I like {i.lower()}, because they can make milk")

    return"I love animals"

animals: list[str] = ["cow","Dog","cAt"]

print(stampa_pizza(animals))