f=[0,1]
x=0
y=1
for i in range(60):
    t=x+y
    f.append(t)
    x=y
    y=t
teste= int(input())
for i in range(teste):
    entrada=int(input())
    print('Fib({}) = {}'.format(entrada, f[entrada]))
