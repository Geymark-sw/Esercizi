def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
    
    chiave_elemento: str = None
    valore_iter: str = None
    
    for i in da_rimuovere.keys():
        chiave_elemento = int(i)
    
    for i in da_rimuovere.values():
        valore_iter = i
    
    new_list: list[int] = []
    

    for i in range(len(lista)):
        
        if lista[i] != chiave_elemento:
            
            new_list.append(lista[i])
            
        elif valore_iter > 0:
            
            valore_iter -= 1
            
        else:
            new_list.append(lista[i])
            
            
        print(valore_iter)

    return new_list
        
 	

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))        