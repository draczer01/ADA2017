from sys import argv
def es_palindromo_iterativo(palabra):
    n = len(palabra)
    result = False
    for i in range(0,n):
        if palabra[i] != palabra[n-1-i]:
            result = False
        if i >= n-1-i:
            result = True
    return  result

def es_palindromo_recursivo(palabra):
    n= len(palabra)
    result = False
    if n < 2:
        result = True
    else:
        if palabra[0] == palabra[n-1]:
                result = es_palindromo_recursivo(palabra[1:n-1])
    return result


p = str(argv[1])
print( 'palabra: ' + str(p))
p_iterativo = es_palindromo_iterativo(p)
print( 'fibonacci iterativo: ' + str(p_iterativo))
p_recursivo = es_palindromo_recursivo(p)
print( 'fibonacci recursivo: ' + str(p_recursivo))