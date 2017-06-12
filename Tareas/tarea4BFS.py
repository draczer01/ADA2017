# BFS y DFS
#archivos necesarios dentro de la carpeta files
# graph.py, InstanciesGenerator.py
# aplicacion de BFS con un closeness centrality
from files import graph
from files import InstanciesGenerator
import random
# se crea una instacioa aleatoria, ene ste caso de un arbol
dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 10)
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 5)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = False )
g = generador.generateInstance('Test', 10, 50)
#se imprime el grafo creado
print(g)

lv = g.vertices
av = random.choice(lv)

cc = g.closenesscentrality(av)
# se calcula la medida de centralidad por cercania de todos los nodos de ese grafo
print([(x, g.closenesscentrality(x)) for x in g.vertices])
