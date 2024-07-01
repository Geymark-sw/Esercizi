def lenght_of_last_word(s: str) -> int:

    s = s.strip   #cancella tutti gli spazi iniziali e finali
    i: int = len(s) - 1
    cont: int = 0

    while i >= 0 :

        if(s[i] != " "):
            cont += 1
        else:
            break    

        i -= 1
       

    return  cont

print(lenght_of_last_word("ciao bello"))