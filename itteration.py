lista = ["nesto", "za", "vezbanje"]

print(lista[0])
print(lista[1])
print(lista[2])

for x in lista:
    print(x)

rotator = iter(lista)

print(next(rotator))
print(next(rotator))
print(next(rotator))

dictio = {"Ime" : "Petar", "Prezime" : "Petrovic"}

abc = iter(dictio)

print(next(abc))
