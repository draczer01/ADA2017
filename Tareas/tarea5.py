#flujos y arboles de expancion Ford-fulkerson y grafos densos y grandes
#archivos necesarios dentro de la carpeta files
# graph.py, InstanciesGenerator.py
from files import graph
from files import InstanciesGenerator
import random
# se genera un grafo con densidad alta y con una cantidad de vertices alta
no_vertices = 105 


dd = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, no_vertices-1 )
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, 10)
generador = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = dd, directed = False )

g = generador.generateInstance('Test', no_vertices, round((no_vertices-1)*.8*no_vertices))
# se selccionan al azar 3 vertices para calcular el fluje en ellas
a = random.choice(g.vertices)
b = random.choice(g.vertices)
while len(g.vertices)>2 and b.id == a.id:
    b = random.choice(g.vertices)
# se calcua el flujo maximo entre los 2
mf = g.maxflow(a.id,b.id)
print(g)
print('Max flow: ', a.id, b.id, mf )

