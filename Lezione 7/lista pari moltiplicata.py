def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    
    lista_pari = []
    
    for i in lista_numeri:
        if i%2 == 0:
            lista_pari.append(i)
            
    for i in range(len(lista_pari)):
        
        lista_pari[i] = lista_pari[i] * fattore
        
        
    return lista_pari



 	

print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))