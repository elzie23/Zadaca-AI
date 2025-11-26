def znakovi_stringova(rjecnik):
    novi_rjecnik={}

    for s in rjecnik:
        for c in s:
            if c not in novi_rjecnik:
                novi_rjecnik[c]=[]

            if s not in novi_rjecnik[c]:
                novi_rjecnik[c].append(s)

    return novi_rjecnik

stringovi= ["dobar", "dan"]
print(znakovi_stringova(stringovi))