# Napiši program koji od korisnika traži da unese svoju godinu rođenja, te ispisuje poruku da li je korisnik punoljetan ili ne.


punoljetnost = int(input("Unesite svoju godinu rodenja: "))

if punoljetnost <= 2006:
    print("Vi ste", punoljetnost, "sto znaci da ste punoljetni")
else:
    print("Vi ste", punoljetnost, "sto znaci da niste punoljetni")
