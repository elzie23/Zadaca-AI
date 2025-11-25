x, y = 5, 7

putanja = input("Unesite putanju robota (S, J, I, Z): ").upper()

#za sjever 3 točke, ostale za 1
for i in putanja:
    if i == 'S':
        y += 3
    elif i == 'J':
        y -= 1
    elif i == 'I':
        x += 1
    elif i == 'Z':
        x -= 1
    else:
        print(f"Ignorirana nepoznata naredba: {i}")

print(f"Konačna pozicija robota: ({x}, {y})")
