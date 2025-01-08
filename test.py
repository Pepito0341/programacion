from os import system
system("cls")
total=0
edad=int(input("ingrese su edad"))
if edad <= 12:
    print("su entrada cuesta $500")
    c_e=int(input("ingrese la cantidad de entradas que quiere: "))
    precio=500
    total=c_e*precio
if edad >=13 and edad <=18:
    print("su entrada cuesta $1000")
    c_entradas=int(input("ingrese la cantidad de entradas que quiere: "))
    total=c_e*precio
if edad >= 19 and edad <=64:
    print("su entrada cuesta $2000")
    c_e=int(input("ingrese la cantidad de entradas que quiere: "))
    precio=2000
    total=c_e*precio
if edad >=65:
    print("su entrada cuesta $700")
    c_e=int(input("ingrese la cantidad de entradas que quiere: "))
    total=c_e*precio
print("su total a pagar es: ", total)
