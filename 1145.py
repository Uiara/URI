entrada = input().split(" ")

repet, fim = entrada

x = 1

final=(int(fim)//int(repet))+(int(fim)%int(repet))


for y in range (1,int(final)+1):
    for z in range(1, (int(repet)+1)):
        print(x, end=" ")
        while x <= int(fim):
            x+=1
    print(end="\n")
