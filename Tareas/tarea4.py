# BFS y DFS
from files import graph
from files import InstanciesGenerator
import random
# aplicacion de BFS con un closeness centrality
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 10, 2)
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = True )
g = generador.generateInstance('Test', 10, 50)

print(g)
lv = g.vertices
av = random.choice(lv)

cc = g.closenesscentrality(av)
print([(x, g.closenesscentrality(x)) for x in g.vertices])
 #aplicacion de DFS con un fill bucket Pendiente
