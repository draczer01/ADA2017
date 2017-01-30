from sys import argv
from math import modf
def potencia(base, pot, mod):
    b = 1
    aux = base
    num = pot
    while num > 0:
        if num % 2 ==1:
            b*=aux
            b%=mod
        aux*=aux
        num = num >> 1
    return b

print(argv)
b = int(argv[1])
p = int(argv[2])
m = int(argv[3])
a = potencia(b,p,m)
print( 'resultado algo: ' + str(a))
print( 'resultado manu: ' + str(b**p%m))

