import numpy as np
a = int(input("Digite la base: "))
b = int(input("Digite el exponente: "))
def a_power_b(a,b):
    contP= 1
    CPar= 0
    CImpar = 0
    while a!=0:
        contP = 1
        for i in range(0,b,) :
           contP = contP * a
           if contP % 2 == 0 :
            CPar=CPar + 1
           elif contP % 2 != 0:
             CImpar=CImpar + 1
        print(contP)
        print("Veces par",CPar)
        print("Veces impar",CImpar)
        a = int(input("Digite la base: "))
        b = int(input("Digite el exponente: "))
a_power_b(a,b)
