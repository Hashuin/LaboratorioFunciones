import numpy as np
a = int(input("Digite la base "))
b = int(input("Digite el exponente "))
def a_power_b(a,b):
    contP= 1
    for i in range(0,b-1,) :
        a = a * a
        contP = a
    print(contP)
a_power_b(a,b)
