# Ramificacion y busquedas para optmizacion
# encontrar la mediana en un arreglo no ordenado, prune and search
     
def ps(arr, indx):
    if len(arr) ==1 :
        return arr[0]
    if len(arr)==0:
        return 0    
    p = arr[0]
    menores, mayores = list(), list()
    for c in arr:
        if c < p:
            menores.append(c)
        elif c >= p:            
            mayores.append(c)
    if len(mayores) == len(arr):
        mayores.remove(p)
        menores.append(p)
        print('=',indx, p, menores, mayores)
    if indx < len(menores):           
        result = ps(menores, indx) 
    elif indx >= len(menores):
        result = ps(mayores, indx-len(menores))
    return result

import random
l = 11
a = list()

for n in range(l):
    a.append(random.randint(0,l))

print(a)
mediana = ps(a, len(a)//2)
print(mediana)
print(sorted(a))
