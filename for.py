from os import system
system("cls")
# for i in range(1,4):
#     print(i)
    
# total=0
# for i in range(3):
#     print("ingrese gasto")
#     gasto=int(input())
#     total=total+gasto
# print(total)
# for i in range(10):
#     print(" ")
#     for j in range(10):
#         print(j+1 , "x", i+1,"=",(i+1)*(j+1))
# cant_años=int(input())
# for i in range(1,20):
#     print(f"usted tiene {i+1} años ")
# total=0
# for i in range(3):
#     print("ingrese 3 numeros")
#     num=float(input())
#     total=total+num
# print(total/3)
total=0
for i in range(3):
    print("ingrese una nota")
    nota=int(input())
    total=total+nota
print("Su promedio es ", total/(i+1))
