print("Aastaaeg") #parandasin "" ära
kuu=int(input("Sisesta kuu number (1-12) => "))
if kuu<1 or kuu>12: # peab olema or
    print("Vigane kuu")
elif kuu<=12 or kuu<=2: #lisasin :
    print("kevad")
elif 3<=kuu<=5:
    print("talv")
elif 6<=kuu<=8:
    print("Suvi")
else:
    print("Sügis")

print("Kiiruse kontroll")
lubatud=int (input("Sisesta lubatud kiirus (km/h) => "))
kiirus= int (input("Sisesta tegelik kiirus (km/h) => "))
yletus= kiirus-lubatud
if yletus <0:
    print("Kiirust ei ületatud")
elif yletus>0:
    print("trahv")
elif yletus>25: # tema sõitis 75 ja sai trahvi
    print("hoiatus")
elif yletus>40:
    print("Juhiluba võetakse ära")

print("Taksosõit")
km = float(input("Sisesta sõidu pikkus (km) => "))
oo = input("Kas sõit on öösel (jah/ei)? => ")
hind= 3+ km + 0.2
if oo=="jah" and oo=="JAH": #lisasin 
    hind=hind*1.2
print("Sõidu hind:", round(hind,2), "€") #lisasin()
