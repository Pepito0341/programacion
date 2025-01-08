from os import system
system("cls")
total=2000
r=input("pertenece a la florida?: ")
if r == "si":
    print("continue a la siguiente")
elif r == "no":
    print("gracias por visitar")
c=input("tiene carnet de socio?: ")
if c=="si":
    (input("ingrese su numero: "))
elif c=="no":
    print("cree su carnet acá")
f=input("es jubilado?: ")
if f =="no":
    print("paga monto total", total)
elif f=="si":
    print("paga monto de", round(total*0.75))
