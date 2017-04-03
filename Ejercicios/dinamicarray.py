from random import choice, randint

def azar(n):
    return [choice(['e', 'i']) for r in range(n)]

def burst(k, minb, maxb):
    op = 'i'
    s = []
    for b in range(k):
        s += [op for x in range(randint(minb, maxb))]
        if op == 'i':
            op = 'e'
        else:
            op = 'i'
    return s


arriba = 0.85
abajo = 0.2

def procesa(secuencia):
    costo = 0
    llenado = 0
    tamanio = 16
    mayor = tamanio
    for operacion in secuencia:
        if operacion == "i":
            llenado += 1
            if llenado / tamanio > arriba:
                tamanio *= 2
                costo += llenado
                if tamanio > mayor:
                    mayor = tamanio
                    print(mayor)
        else:
            llenado -= 1
            if llenado < 0:
                llenado = 0
            if llenado / tamanio < abajo:
                tamanio /= 2
                costo += llenado
    return costo

k = 30
secuencia = burst(k, 10, 60)
n = len(secuencia)
print("burst", procesa(secuencia) / n)
print("azar ", procesa(azar(n)) / n)

