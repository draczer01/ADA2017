# BFS y DFS
import files.graph
import files.InstanciesGenerator
import random
# aplicacion de BFS con un closeness centrality
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 10, 2)
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 2, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.tree,distribution_weight = dw,distribution_degree = dd, directed = True )
g = generador.generateInstance('Test', 10, 50)
lv = g.vertices
av = random.choice(lv)

g.closenesscentrality(av)
 #aplicacion de DFS con un fill bucket Pendiente
