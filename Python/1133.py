#Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

primeiro = int(input())
segundo = int(input())
lista = []


if primeiro > segundo:
   for x in range(segundo+1, primeiro):
       if (x % 5 == 2) or (x % 5 == 3):
           lista.append(x) 

if primeiro < segundo:
    for x in range(primeiro+1, segundo):
        if (x % 5 == 2) or (x % 5 == 3):
           lista.append(x) 

for x in lista:
    print(x)

