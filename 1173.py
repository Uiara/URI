while True:
    entrada = int(input())
    if entrada > 50:
        break
    for x in range(10):
        if x == 0:
            print('N[{}] = {}'.format(x,entrada))
        else:
            entrada *= 2
            print('N[{}] = {}'.format(x,entrada))
    break