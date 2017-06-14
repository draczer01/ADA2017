#Aleatorizacion
# se trabajo el problea de vertex cover
#archivos necesarios dentro de la carpeta files
# graph.py, InstanciesGenerator.py
from files import graph
from files import InstanciesGenerator
from heapq import heappop, heappush
import random
# se crea un grafo conecntado con nu valor de nuemero de vertices y el numero de veces que se ejecutara la aproximacion
no_cycles = 10
no_vertices = 20


dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, no_vertices )
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = True )

g = generador.generateInstance('Test', no_vertices, no_vertices * 1.5)
print(g)
#print('con',g.connected)
for i in range(no_cycles):

    scover = set()
    covered = set()
    
    edg = list(g.getedges().keys())
# se seleccionan 1 arista al azar del conjunto de aristas, se agregan los vertices al cubrimiento y se eliminan las aristas incidentes a los vertices, se repete hasta tener un cubrimiento de todas las aristas
    while len(edg) > 0:
#        print(len(edg))
        se = random.choice(edg)
        #print(se)
        scover.add(se[0])
        scover.add(se[1])
        se1, se2 = False, False
        for e in edg:
            r = False
            if se[0] in e:
                #print(se, e, se[0] in e, se[1] in e, len(edg))
                se1=True
                r=True
            if se[1] in e:
                se2=True
                r=True
            if r:
                edg.remove(e)
        if not se1:
            scover.remove(se[0])
        if not se2:
            scover.remove(se[1])
    #se imprime el cubrimiento
    print( i, len(scover))
