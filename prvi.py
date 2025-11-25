import random
i=0
lista = []
while i < 100:
    lista.append(random.randint(0, 30)) #uključujući 0 i 30
    i += 1

print(lista)
ponavljanja = 0


for i in range(len(lista)):
    if lista[i] in lista[:i]:
        continue

    ponavljanja = 1  

    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            ponavljanja += 1

    if ponavljanja >= 3:
        print(f"Broj {lista[i]} se ponavlja {ponavljanja} puta.")
