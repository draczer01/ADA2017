costo = 0
from random import random

def qs(arr):
    global costo
    if len(arr) < 2:
        return arr # base case
    p = arr.pop(0)
    menores, mayores = list(), list()
    for c in arr:
        if c <= p:
            costo += 1
            menores.append(c)
        elif c > p:
            costo += 1
            mayores.append(c)
    return qs(menores) + [p] + qs(mayores) 
    

def rndar(lon):
    arr = []
    for r in range(lon):
        arr.append(random())
    return arr

l = 8
while l < 10000:
    for replica in range(30):
        qs(rndar(l))
        print(l, costo)
        costo = 0
    l *= 2
   
