#Aleatorizacion
# vertex cover
from files import graph
from files import InstanciesGenerator
from heapq import heappop, heappush
import random

no_cycles = 10
no_vertices = 15


dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 25 )
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = True )

g = generador.generateInstance('Test', no_vertices, no_vertices * 1.5)
print(g)
#print('con',g.connected)
for i in range(no_cycles):

    scover = set()
    covered = set()
    
    edg = list(g.getedges().keys())

    while len(edg) > 0:
#        print(len(edg))
        se = random.choice(edg)
        #print(se)
        scover.add(se[0])
        scover.add(se[1])
        for e in edg:
            if se[0] in e or se[1] in e:
                #print(se, e, se[0] in e, se[1] in e, len(edg))
                edg.remove(e)
    
    print('res ', i, ' ', scover, len(scover))
