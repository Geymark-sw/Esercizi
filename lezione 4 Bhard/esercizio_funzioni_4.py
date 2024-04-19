def check_each(l:list):

    for i in l:
        if i > 5:
            print(f"Il numero {i} è maggiore di 5")

        elif i < 5:
            print(f"Il numero {i} è maggiore di 5")

        else:
            print(f"Il numero {i} è uguale a 5")

l:list = [2,5,10,]

check_each(l)