def generatore():

    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()
print(next(prova_generatore))
print(next(prova_generatore))
    