# Napiši program koji omogućava korisniku unos cijelog broja, a potom provjerava da li je zadnja cifra broja djeljiva sa 3.

a = int (input("Unesite dvocifren broj: "))

zadnja_cifra=a%10
if zadnja_cifra/4:
    print(f"Vasa zadnja cifra {zadnja_cifra} je djeljiva sa 4")
else:
   print(f"Vasa zadnja cifra {zadnja_cifra} nije djeljiva sa 4")
