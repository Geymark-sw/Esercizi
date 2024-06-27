

def decorator(func):

    def wrapper(*args):
        import time

        start = time.time()

        func(*args)
        print(f"Time elapsed: {time.time() - start}")

    return wrapper



# @decorator
# def area_cerchio(raggio: float):

#     return raggio * raggio * 3.14

# area_cerchio(1)

