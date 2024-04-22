def majority_element(nums: list[int]) -> int:

    """
        Data una lista di n elementi, restituire l'elemento che compare più di n/2 volte
        dove n = alla dimensione della lista
    """

    cont: int = 0
    cont_max: int = 0
    num_max: int = None

    for i in nums:
        for j in nums:
            if i == j :
                
                cont += 1

        if cont > cont_max:
                
            cont_max = cont
            num_max = i

    if cont_max > len(nums)/2:

        return num_max
    else:
        return None
    
l: list[int] = []

while(True):
    l.append(int(input("Inserisci un numero:")))

    ver: str = input("Vuoi inserire un nuovo numero nella lista? si/no ")

    if ver.lower() != "si":
        print(majority_element(l))
        break


