n = int(input())
entrada = input()
lista = [int(x) for x in entrada.split()]
print("Menor valor: {}\nPosicao: {}".format(min(lista),lista.index(min(lista))))