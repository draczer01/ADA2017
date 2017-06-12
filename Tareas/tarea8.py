# Transicion de fase
# Se revisó la transicion de fase de la centralidad por cercania contra la densidad de una grafo no dirigido , ya que mostraba una transicion de fase al trabajar con grafos completos de 50 aristas o menos

# generador de instancias de grafos
from files import graph
from files import InstanciesGenerator
import random
import time

#funcion que ejecuta y mide la centralidad por cercania para todos los nodos
def exe(g,de=0):
    g#0 = generadortree.generateInstance(name + ' tree', n, m1)
    g.connected
    g.complete
    g.tree
    av = random.choice(list(g.vertices))
    tt0 = time.clock()
    cct =g.closenesscentrality()
    tt1 = time.clock()
    tc = (tt1-tt0)*1000.0
    #informacion que se toma en cuenta, densidad y tiempo de ejecucion de la cc
    print( str(de) , str(tc))
    del g
    return d

#Definicion de los parametros,
#Nombre
name = 'test'
direct = False
#Numero de vertices
n= 50
cycle = 100
dl, du = 1 , n
wl, wu = 1, 10

# Distribucion de los grados
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, dl, du)
#Distribucion de los pesos
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, wl, wu)

generadorcomplete = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.complete,distribution_weight = dw,distribution_degree = dd, directed = direct )

generadorconnected = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = direct )

generadortree = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = direct )

#incio del ciclo
for i in range(cycle):
    # se genera un arbol, apra comenzar a medir el tiempo
    g0 = generadortree.generateInstance(name + ' tree', n, n-1)
    exe(g0, (g0.density)*100.0)
    #ahora, aumentando al densidad del grafo de 5 en 5, calcularemos su CC
    d = 5    
    while d < 100:
        g1 = generadorconnected.generateInstance(name + ' connected', n, (n*(n-1)*d/100))
                
        exe(g1,d)
        d += 5
    #por ultimo calcularmos el tiempo de un grafo completo
    gc = generadorcomplete.generateInstance(name + ' complete', n, n)
    exe(gc,(gc.density)*100.0)

# se generaron varios resultados para los valores de 50 aristas, mientras que para tamaños mayores se perdia la transicion de fase.
