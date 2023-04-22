while True:
    entrada = int(input())
    cont = 0
    total = 0
    if entrada == 0:
        break
    while cont < 5:
        if entrada % 2 == 0:
            total += entrada
            cont += 1
            entrada += 1
        else:
            entrada += 1
    print(total)