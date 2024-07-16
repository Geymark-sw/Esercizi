def decorator(func):

    def wrapper():

        print("Prima della funzione")

        func()

        print(f"Dopo la funzione")

    return wrapper

def func():

    print("ciao")


func()

func = decorator(func)   # stessa cosa di scrivere sulla definizione della funzione @nomeDecorator

func()