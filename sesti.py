import math

def na_kruznici(x, y, a, b, r, tol=1e-9):
    return math.isclose((x-a)**2 + (y-b)**2, r**2, abs_tol=tol)

a = float(input("unesite x koordinatu centra kruznice: "))
b = float(input("unesite y koordinatu centra kruznice: "))
r = float(input("unesite polumjer kruznice: "))

tocke = []

print("Unesite 10 tocaka, za prekid unesite tocku 0 0")
for i in range(10):
    print(f"Tocka {i+1}:")
    x= float(input("x: "))
    y= float(input("y: "))

    if x == 0 and y == 0:
        print("Prekid unosa")
        break

    tocke.append((x,y))

broj_pogodaka = 0

for x, y in tocke:
    if na_kruznici(x, y, a, b, r):
        print(f"Tocka ({x}, {y}) je na kruznici.")
        broj_pogodaka += 1
    else:
        print(f"Tocka ({x}, {y}) nije na kruznici.")

if len(tocke) > 0:
    omjer = (broj_pogodaka / len(tocke)) * 100
    print(f"Omjer pogodaka kruznice: {omjer:.2f}%")
else:
    print("Nema unesenih točaka.")