def prosjek(rjecnik):
    novi_rjecnik={}

    for ime, ocjene in rjecnik.items():
        prosjek=round(sum(ocjene)/len(ocjene))
        
        if prosjek not in novi_rjecnik:
            novi_rjecnik[prosjek]=[]
        novi_rjecnik[prosjek].append(ime)

    for i in novi_rjecnik:
        novi_rjecnik[i].sort()
    
    return novi_rjecnik

rjecnik= {'ivan': (3,2,4), 'marko': (5,5,4), 'ana': (2,3,4)}
print(prosjek(rjecnik))