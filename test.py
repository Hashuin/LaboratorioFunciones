
import numpy as np 
n = int(input("Ingrese un numero: "))
def numero_perfecto(n):
  cont = 0
  for i in range(1,n): 
    if n%i==0 :
      cont+=i

    if cont==n :
      print("El numero es perefecto")
    else :
      print("El numero no es perfecto")
numero_perfecto(n)