def filtriraj_po_visini(rjecnik, min_v):
    novi_rjecnik = {}
    for ime, visina in rjecnik.items():
        if visina > min_v:
            novi_rjecnik[ime] = visina
    return novi_rjecnik

rjecnik={'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190} 

print(filtriraj_po_visini(rjecnik, 165))