current_users: list[str] = ["pippo","pluto","admin","topolino","jhon cena"]
new_users: list[str] = ["ciaone","pluto","KimJongUn","topOlino","jhon cena"]

for i in new_users:

    for j in range(len(current_users)):

        if i.lower() != current_users[j].lower() and j == len(current_users)-1:

            print(f"Lo user-name '{i}' è disponibile")
            
        elif i.lower() == current_users[j].lower():
            print(f"Lo user-name '{i}' NON è disponibile. Ti prieghiamo di cambiarlo")
            break
 

