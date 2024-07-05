valor = input().split(" ")
valor1 = input().split(" ")

x1, y1 = valor
x2, y2 = valor1

distancia=(((float(x1) - float(x2))**2) + ((float(y1) - float(y2))**2))
raizQ = distancia ** ( 1 / 2 )

print("%.4f"%raizQ)
