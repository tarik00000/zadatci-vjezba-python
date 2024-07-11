# Učenik ne može izaći na ispit ako je prisustvao manje od 75% časova. Napiši program koji od korisnika traži da 
# unese broj održanih časova i broj časova na kojima je prisustvovao, a zatim ispisuje postotak njegovog prisustva te da li može izaći na ispit ili ne.

broj_casova = int(input("Unesio borj odrzanih casova: "))
prisustvo = int(input("Unesi broj prisustva: "))

postotak=(prisustvo/broj_casova)*100
if postotak >= 75:
    print(f"Vas postotak prisustva je {postotak}% mozete da izdete na ispit")
else:
    print(f"Vas postotak prisustva je {postotak}% ne mozete da izdete na ispit")