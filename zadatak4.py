# Napiši program koji unosi tri cijela broja i ispisuje najveći od njih.

a=int(input("Unesi jedan broj: "))
b=int(input("Unesi drugi broj: "))
c=int(input("Unesi treci broj: "))

if a>b and a>c:
    print(a, "je najveci broj")
elif b>a and b>c:
    print(b, "je najveci broj")
if c>b and c>a:
    print(c, "je najveci broj")
else:
    print(f"Vasi brojevi {a,b,c} su svi jednaki")