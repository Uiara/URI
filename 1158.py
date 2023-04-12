quantidade_teste = int(input())

for i in range (quantidade_teste):
    x, y = map(int, input().split())
    total = 0
    if y > 0:
        z = 0
        while z < y:
            if x % 2 != 0:
                total += x
                z += 1
            x += 1
    print(total)

