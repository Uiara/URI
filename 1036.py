import math

entrada= input().split(" ")

a, b, c = entrada

a = float(a)
b = float(b)
c = float(c) 

if a and b and c <= 0:
    print("Impossivel calcular")
else: 
    passo1 = (-1 * b)
    passo2 = (b**2) - ((4*a)*c)
    passo3 = math.sqrt(passo2)
    passo4 = 2*a
    soma = ((passo1 + passo3) / passo4)
    subritacao = ((passo1 - passo3)/passo4)
    print("R1 = %.5f\nR2 = %.5f"%(soma, subritacao)) 
