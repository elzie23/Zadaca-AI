import random

lista=[]
i=0
while i < 50:
    lista.append(random.randint(1, 999))
    i += 1
print("Lista brojeva:", lista)

frekvencija = {}

for broj in lista:
    for znamenka in str(broj):
        z = int(znamenka)
        frekvencija[z] = frekvencija.get(z, 0) + 1

print(f"Rjecnik frekvencije: {frekvencija}")

print("Frekvencija znamenki:")

for k, v in sorted(frekvencija.items()):
    print(f"{k} - {v} puta")
