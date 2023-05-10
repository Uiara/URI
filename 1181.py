# leitura da linha a ser considerada
linha = int(input())

# leitura da operação a ser realizada
operacao = input()

# inicialização da matriz com os valores de entrada
M = []
for i in range(12):
    linha_i = []
    for j in range(12):
        valor = float(input())
        linha_i.append(valor)
    M.append(linha_i)

# seleção dos elementos da área verde
elementos_verdes = []
for j in range(12):
    if j > linha:
        break
    elementos_verdes += M[linha][j+1:]

# cálculo da soma ou média dos elementos verdes
if operacao == 'S':
    resultado = sum(elementos_verdes)
else:
    resultado = sum(elementos_verdes) / len(elementos_verdes)

# impressão do resultado com uma casa decimal
print('{:.1f}'.format(resultado))
