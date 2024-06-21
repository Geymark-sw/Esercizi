def decorator(func):

    def wrapper():

        import time

        start = time.time()

        func()

        print(f"Dopo la funzione")

    return wrapper

    