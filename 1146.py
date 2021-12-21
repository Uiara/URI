#Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). 
# Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.


while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        for i in range(1,entrada):
            print(i,end=" ")
        print(entrada,end="\n")