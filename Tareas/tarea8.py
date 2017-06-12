
# generador de instancias de grafos
from files import graph
from files import InstanciesGenerator
import random
import time


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
    #print(g0.to_string(sv=False))
    d = (g.density)*100.0
    tt0 = time.clock()
    bfst =g.breadthfirstsearch()
    tt1 = time.clock()
    tb = (tt1-tt0)*1000.0
    print( str(de) , str(tc), str(tb) )
    del g
    return d


#Nombre
name = 'test'
direct = False
#Numero de vertices
n= 50
cycle = 10
dl, du = 1 , n
wl, wu = 1, 10

# Distribucion de los grados
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, dl, du)
#Distribucion de los pesos
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, wl, wu)

generadorcomplete = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.complete,distribution_weight = dw,distribution_degree = dd, directed = direct )

generadorconnected = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = direct )

generadortree = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = direct )

for i in range(cycle):
    g0 = generadortree.generateInstance(name + ' tree', n, n-1)
    exe(g0, (g0.density)*100.0)
    d = 5
    while d < 100:
        g1 = generadorconnected.generateInstance(name + ' connected', n, (n*(n-1)*d/100))
                
        exe(g1,d)
        d += 5
    
    gc = generadorcomplete.generateInstance(name + ' complete', n, n)
    exe(gc,(gc.density)*100.0)
  
