valor = int(input(""))
resto = 0

if 0 < valor < 1000000:
    n100 = int(valor // 100)
    resto = valor % 100

    n50 = int(resto // 50)
    resto = resto % 50

    n20 = int(resto // 20)
    resto = resto % 20

    n10 = int(resto // 10)
    resto = resto % 10

    n5 = int(resto // 5)
    resto = resto % 5

    n2 = int(resto // 2)   
    resto = resto % 2
    
    n1 = int(resto // 1)
    resto = resto % 1

print("{}".format (valor))
print("{} nota(s) de R$ 100,00".format(n100))
print("{} nota(s) de R$ 50,00".format(n50))
print("{} nota(s) de R$ 20,00".format(n20))
print("{} nota(s) de R$ 10,00".format(n10))