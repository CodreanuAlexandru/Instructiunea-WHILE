n=0
sp=0
sn=0
np=0
nn=0
l=0
while l<12:
    n=eval(input("Introduceti temperatura:"))
    if n<55 and n>-60:
        l+=1
        if n>0:
            sp+=n
            np+=1
        elif n<0:
            sn+=n
            nn+=1 
    else: print("Error: Introduceti o temperatura valida")           
if np>0:
    print("medie_poz=",sp/np,)
else:print("Nu au fost temperaturi pozitive")
if nn>0:
    print("medie_neg=",sn/nn,)
else:print("Nu au fost temperaturi negative")