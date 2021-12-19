cont = 0
notaInicial = 0
while True:
    nota = float(input())
    
    while nota <= 0.0 or nota >= 10.0:
        print("nota invalida")
        nota = float(input())
        if nota > 0 or nota < 10:
            cont += 1
            notaInicial += nota
            break
    if cont == 2:
        media = notaInicial / cont
        print("media = {:.2f}".format(media))
        novaEntrada = int(input("novo calculo (1-sim 2-nao)"))
        while novaEntrada != 1 and novaEntrada != 2:
            novaEntrada = int(input("novo calculo (1-sim 2-nao)"))
        if novaEntrada == 1:
            cont = 0
            nota = 0
            notaInicial = 0
        elif novaEntrada == 2:
            break
    else:
        break