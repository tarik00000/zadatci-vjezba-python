#Napiši program koji ispituje da li je trougao jednakostranični, jednakokraki ili raznostranični.

a = int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))
c = int(input("Unesi treci broj: "))

if a==b and a==c:
    print(f"Vas trougao {a,b,c} je jednakostranicni")
elif a==b  and b!=c:
    print(f"Vas trougao {a,b,c} je jednakokraki")
else:
    print(f"Vas trougao {a,b,c}, je raznostranicni")
