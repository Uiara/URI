s = 0
z = 1
for x in range(1,41,2):
    s += x/z
    z *= 2  
    
print("%0.2f"%s)
