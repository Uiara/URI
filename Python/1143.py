#Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

n = int(input())
x = 1

for y in range (1,n+1):
    print("{} {} {}".format(x,x**2,x**3))
    x += 1
