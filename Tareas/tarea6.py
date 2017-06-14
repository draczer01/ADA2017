# Ramificacion y busquedas para optmizacion
# encontrar la mediana en un arreglo no ordenado, prune and search
#funcion prune and search. es como un quickshort solo que buscando el elemento numero indx del arreglo ordenado
import random
costo1 = 0
costo2 = 0

def ps(arr, indx):
    global costo1
    if len(arr) ==1 :
        return arr[0]
    if len(arr)==0:
        return 0    
    p = arr[0]
    menores, mayores = list(), list()
    for c in arr:
        if c < p:
            costo1 += 1
            menores.append(c)
        elif c >= p:
            costo1 += 1            
            mayores.append(c)
    if len(mayores) == len(arr):
        costo1+=1
        mayores.remove(p)
        menores.append(p)
    if indx < len(menores):           
        result = ps(menores, indx) 
    elif indx >= len(menores):
        result = ps(mayores, indx-len(menores))
    return result

def qs(arr):
    global costo2
    if len(arr) < 2:
        return arr # base case
    p = arr.pop(0)
    #costo2 +=1
    menores, mayores = list(), list()
    for c in arr:
        if c <= p:
            costo2 += 1
            menores.append(c)
        elif c > p:
            costo2 += 1
            mayores.append(c)
    return qs(menores) + [p] + qs(mayores) 


# fn que crea un arreglo de l elementos, que van de 0 hasta l
def rndar(lon):
    arr = []
    for r in range(lon):
        arr.append(random.randint(0, lon))
    return arr

l = 50
upper = 15000
replicas = 30
while l< upper:
    for r in range(replicas):
        # se crea un arreglo desordenado
        a = rndar(l)        
        #print(a)
        #se busca la mediana del arreglo
        m = len(a)//2
        mediana = ps(a, m)
        #print(mediana)
        # se ordena el arreglo para corroborar
        ol =qs(a)
        #print('m:',mediana,'om: ',ol[m], 'l:', m)
        #print(ol,'mediana:', ol[m])
        assert mediana == ol[m]
        # se imprime tiempos, se agrega 1 al costo del quickshort por la busqueda del indice
        print(l, costo1,costo2+1, )
    l*=2
