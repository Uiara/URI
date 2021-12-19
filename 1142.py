#Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

n = int(input())
x = 1

for y in range (1,n+1):
    print("{} {} {} PUM".format(x,x+1,x+2))
    x += 4