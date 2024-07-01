cane : dict[str:str] = {"tipo":"Cane","proprietario":"Grace"}
gatto: dict[str:str] = {"tipo":"Gatto","proprietario":"Wilton"}
pappagallo: dict[str:str] = {"tipo":"Pappagallo","proprietario":"Cristian"}
capybara: dict[str:str] = {"tipo":"Capybare","proprietario":"Giuse"}

lista: [dict[str:str]] = [cane,gatto,pappagallo,capybara]

for i in lista:

    print(i)