lista = []
for x in range(20):
    entrada = int(input())
    lista.append(entrada)
lista.reverse()
for y in range(20):
    print("N[{}] = {}".format(y,lista[y])) 
