a=int(input("Kérem a háromszög első oldalát!"))
b=int(input("Kérem a háromszög második oldalát!"))
c=int(input("Kérem a háromszög harmadik oldalát!"))
if(a<b+c)and(b<a+c)and(c<a+b):
    print("A háromszög szerkeszthető!")
else: print("A háromszög nem szerkeszthető!")