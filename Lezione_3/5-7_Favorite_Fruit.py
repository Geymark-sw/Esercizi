favorite_fruits: list[str] = ["mango","ananas","litchi"]

verifica_frutta: list[str] = ["mela","banana","mango","litchi","frutto del drago"]

for i in verifica_frutta:

    if i in favorite_fruits:

        print(f"You really like {i}")
    else:

        print(f"L'elemento {i} non è presente nella lista favorite_fruits")