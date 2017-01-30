from sys import argv
def fibonacci_recursivo(n):
    if n < 2 :
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    if n < 2:
        return n
    a0, a1 = 0, 1
    for i in range(2,n+1):
        a1, a0 = a0 + a1, a1
    return a1

a = int(argv[1])
print( 'numero: ' + str(a))
fiboIterativo = fibonacci_iterativo(a)
print( 'fibonacci iterativo: ' + str(fiboIterativo))
fiboRecursivo = fibonacci_recursivo(a)
print( 'fibonacci recursivo: ' + str(fiboRecursivo))