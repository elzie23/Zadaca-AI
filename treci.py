import random

def loto642():
    brojevi = random.sample(range(1, 43), 7)  # 6 + dopunski
    return brojevi

igracevi = []
print("\nUnesite 6 brojeva igrača (od 1 do 42):")
for i in range(6):
    broj = int(input(f"Broj {i+1}: "))
    igracevi.append(broj)

brojevi = loto642()

izvuceni = brojevi[:6]
dopunski = brojevi[6]

print("Izvučeni brojevi:", *izvuceni) #ispisani bez zagrade
print("Dopunski broj:", dopunski)

pogodjeno = [b for b in igracevi if b in izvuceni]

print("Pogodjeni brojevi:", *pogodjeno)
print("Broj pogodaka:", len(pogodjeno))

if pogodjeno:
    print("Suma pogođenih brojeva:", sum(pogodjeno))
    print("Najmanji pogođeni broj:", min(pogodjeno))
    print("Najveći pogođeni broj:", max(pogodjeno))
else:
    print("Nema pogođenih brojeva, pa nema min/max/sume.")
