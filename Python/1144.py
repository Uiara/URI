n = int(input())
x = 1
for y in range (1,n+1):
    print("{} {} {}".format(x, x*x,x*x*x))
    print("{} {} {}".format(x,x*x+1,x*x*x+1))
    x += 1