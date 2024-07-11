# Napiši program koji od korisnika traži da unese godinu, te ispisuje da li je ona prestupna ili ne. 
# *Napomena: Da bi godina bila prestupna mora ispuniti jedan od dva uslova:
# Djeljiva sa 4 ali ne sa 100 
# Djeljiva sa 400

godina = int(input("Upisite neku godinu: "))


if godina%4 == 0 and godina%100 != 0 or godina%400 == 0:
    print(f"Vasa izabrana godina {godina} je prestupna")
else:
    print(f"Vasa izabrana godina {godina} nije prestupna")
    