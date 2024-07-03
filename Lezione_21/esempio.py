def generatore():

    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()
print(next(prova_generatore))
print(next(prova_generatore))

from contextlib import contextmanager
import time

@contextmanager
def context_manager():

    start_time: float = time.time()

    yield
    end_time: float = time.time()
    elapsed_time: float = end_time - start_time

    print(f"{elapsed_time=}")




import sys

a = []

b = a
print(sys.getrefcount(a))


threads: list = []

def thread_function(name):

    print(f"{name} Time - {time.time()}")

    time.sleep(2)

    print(f"{name} Time - {time.time()}")


import threading
import random

def funzione(id: int):
    sleep_time: int = random.randint(1,10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")

if __name__ == "__main__":
    
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=10) as esecutor:
    
        esecutor.map(funzione, range(100))



for i in range(3):

    x = threading.Thread(target=thread_function, args=(i,))
    threads.append(x)
    x.start()

for i in threads:
    
    i.join()

print(f"Prima di thread")
x.start()
print(f"Thread partito")
x.join()
print(f"Thread finito????")



    