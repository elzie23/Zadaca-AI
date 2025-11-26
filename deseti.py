lista = ['abc', 'aba', 'cc', 'ijki'] 
br_zn=0
brojac=0

for i in lista:
    if len(i) >=3:
        for j in i:
            if j==i[0]:
                br_zn +=1
        if br_zn>=2:
            brojac +=1
    br_zn=0
    
print(brojac)