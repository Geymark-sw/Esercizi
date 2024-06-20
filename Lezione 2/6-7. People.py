dizionario: dict[str:object] = {"first_name":"Geymark Emmanuel", "last_name":"Papio", "age":20, "city": "Roma"}

cristian: dict[str:str] = {"first_name":"Cristian", "last_name":"Salazar", "age":20, "city":"Lima"}

giuseppe: dict[str:str] = {"first_name":"Giuseppe", "last_name":"Taverna", "age":17, "city": "Napoli"}

lista_dizionari_persone: list[dict] = [dizionario, cristian, giuseppe]

for i in lista_dizionari_persone:

    print(i["first_name"] + " " + i["last_name"])
    print(i.items())

