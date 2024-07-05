#Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). 
# Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).
x = 0
lista = []

while True:
    x = 0
    lista = []

    M,N = map(int, input().split())

    if M <= 0 or N <= 0:
        break

    if M == N:
        x = M
        lista.append(x)
        print("{} Sum={}".format(x,x))
        continue


    if M >= N:
        x = M
        lista.append(x)
        x -= 1
        while x != N:
            lista.append(x)
            x-=1
        lista.append(N)



    if N >= M:
        x = N
        lista.append(x)
        x -= 1
        while x != M:
            lista.append(x)
            x-=1
        lista.append(M)
    lista.reverse()


    soma = 0
    for x in  lista:
        print(x, end=' ')
        soma += x
    print("Sum={}".format(soma))
    lista.clear()



