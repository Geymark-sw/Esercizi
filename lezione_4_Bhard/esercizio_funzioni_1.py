def check_value(a):
    if a > 5:
        print(f"Il numero {a} è maggiore di 5")

    elif a < 5:
        print(f"Il numero {a} è minore di 5")

    else:
        print(f"Il numero {a} è uguale a 5")

a: float = int(input("Inserisci il numero: "))