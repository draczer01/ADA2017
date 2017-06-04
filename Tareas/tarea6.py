# Ramificacion y busquedas para optmizacion
# encontrar la mediana en un arreglo no ordenado, prune and search
     
def ps(arr, indx):
    #global costo
    if len(arr) ==1 :#and indx ==1:
        return arr[0]
    if len(arr)==0:
        return 0    
    p = arr[0]
    menores, mayores = list(), list()
    for c in arr:
        if c < p:
            #costo += 1
            menores.append(c)
        elif c >= p:
            #costo += 1
            mayores.append(c)
    #print(indx, p, menores, mayores)

    
    #elif indx == len(menores):
    #    result = p
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
    #a.append(n)
    a.append(random.randint(0,l))
#random.shuffle(a)
#a = [0,2,3,1,4]

print(a)

mediana = ps(a, len(a)//2)
#print(a)
print(mediana)

print(sorted(a))
