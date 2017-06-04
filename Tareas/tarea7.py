#Aleatorizacion
# vertex cover
from files import graph
from files import InstanciesGenerator
from heapq import heappop, heappush
import random

no_vertices = 15 


dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 2 )
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 2)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = True )

g = generador.generateInstance('Test', no_vertices, 20)
print(g)
#print('con',g.connected)
if g.connected:
    scover = set()
    covered = set()
    while len(covered) < g.cardinal:
        print(len(covered), g.cardinal)
        cl = []
        for v in g.vertices:
            a = (len(set(g[v].neighbors) - covered),v)
            cl.append(a)
        m, vv = max(cl, key=lambda k:k[0])
        scover.add(vv)
        covered.add(vv)
        for x in g[vv].neighbors.keys():
            covered.add(x)
    print('res',scover,len(scover))
else:
    print('not connected')        
