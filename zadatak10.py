# Napiši program koji omogućava korisniku da unese masu i visinu, a potom računa indeks tjelesne mase (BMI) 
# te ispisuje u kojoj kategoriji se nalazi na osnovu tabele ispod. Indeks tjelesne mase računamo 
# po formuli: BMI = MASA [kg] / VISINA^2 [m] 
# BMI	        STATUS
# < 19.1	    prenizak
# 19.2 – 25.8	idealan
# 25.9 – 27.3	blago povišen
# 27.4 – 32.2	visok
# 32.3 – 44.8	previsok
# > 44.9	    izrazito visok

masa = int(input("Unesite masu: "))
visina = float(input("Unesite visinu: "))
bmi = masa/visina**visina

if bmi < 19.1:
    print(f"Vas status {bmi} jeprenizak")
elif bmi < 19.2 and bmi > 25.8:
    print(f"Vas status {bmi} je idealan")
elif bmi < 25.9 and bmi > 27.3:
    print(f"Vas status {bmi} je blago povisen")
elif bmi < 27.4 and bmi > 32.2:
    print(f"Vas status {bmi} je visok")
elif bmi < 32.3 and bmi > 44.8:
    print(f"Vas status {bmi} je previsok")
elif bmi > 44.9:
    print(f"Vas status {bmi} je izrazito visok")