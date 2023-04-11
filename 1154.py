#Faça um algoritmo para ler um número indeterminado de dados, 
# contendo cada um, a idade de um indivíduo. 
#O último dado, que não entrará nos cálculos, contém o valor de idade negativa. 
#Calcular e imprimir a idade média deste grupo de indivíduos
lista = []
while True:
    x = int(input())  
    if x < 0:
        print("%.2f" %(sum(lista)/len(lista)))
        break
    else:
        lista.append(x)