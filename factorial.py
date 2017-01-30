from math import log , exp
from sys import argv
def binomial ( n, k, accrt = True):
    may = max(k, n-k)
    men = min(k, n-k)
    up = 0
    down = 0
    if accrt:
        up = 1
        down = 1
    for i in range(may+1, n+1):
        if accrt:
            up *= i
        else:
            up += log(i)

    for j in range(2, men):
        if accrt:
            down *= j
        else:
            down += log(j)
    if accrt:
        return up/down
    else:
        res = up - down
        return exp(res)
print(argv)
a = binomial(int(argv[1]), int(argv[2]), True)
b = binomial(int(argv[1]), int(argv[2]), False)
print( 'ex: ' + str(a))
print('log: ' + str(b))
print( 'dif: ' + str(a - b))
print('%: ' + str((a-b)/a))
