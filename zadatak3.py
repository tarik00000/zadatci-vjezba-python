#Napiši program za automat koji radi na principu unosa broja i ispisa određenog artikla za taj broj prema datoj slici. 
# Ako uneseni broj ne odgovara niti jednom artiklu, ispisati poruku “Broj ne odgovara niti jednom artiklu”. 


table = {
    5: "TWIKS",
    10:"SNICKERS",
    15:"KINDER BUENO",
    20:"GRISINI",
    25:"KIKIRIKI",
    30:"PERECI"
}
a = int(input("Unesite broj da bi dobili vasu narudbu: "))

if a in table:
    print(f"Vasa {table[a]} narudba stize uskoro")
else:
    print("Vas broj koji ste unjeli je nepostojajuci u nasem automatu")
    print("Mozete izabrati", table)