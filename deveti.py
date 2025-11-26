def nebrojcani(matrica):
    novi_rjecnik = {}

    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            e=matrica[i][j]

            if not e.isnumeric():
                novi_rjecnik[(i,j)] = e
    return novi_rjecnik

matrica = [ ["5", "4", "a", "1"], ["c", "3", "12", "b"], ["7", "9", "0", "d"]]
print(nebrojcani(matrica))
