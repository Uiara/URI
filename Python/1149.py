entrada = list(map(int, input().split()))


x = 1
soma = 0

while entrada[x] <= 0:
    if entrada[x] <=0:
        x += 1
    if entrada[x] > 0:
        break

for y in range(0,entrada[x]):
    soma = soma + entrada[0] + y


print(soma)