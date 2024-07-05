
lista = []
for i in range(10):
    entrada = int(input())
    if entrada <= 0:
        entrada = 1
        lista.append(entrada)
    else:
        lista.append(entrada)

for i in range(10):
    print('X[{0}] = {1}'.format(i,lista[i]))