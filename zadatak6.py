#Napiši program za unos jednog broja koji zatim provjerava da li se taj broj nalazi na jednom od intervala: (-1,1], (5,15), [25,46], [59,60).
#Napomena: srednje zagrade u matematici označavaju da je broj uključen u interval, a male da nije.

a = int(input("Unesi neki broj: "))

if a>-1 and a<=1 or a>5 and a>15 or a>25 and a>46 or a<= 59 and a> 60:
    print(f"Vas broj {a} se nalazi u tabeli")
else:
    print(f"Vas broj {a} se ne nalazi u tabeli")