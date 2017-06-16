#flujos y arboles de expancion Ford-fulkerson y grafos densos,grandes y normales
#archivos necesarios dentro de la carpeta files
# graph.py, InstanciesGenerator.py
from files import graph
from files import InstanciesGenerator
import random
import time
# se genera un grafo con densidad alta y con una cantidad de vertices alta, para ver el desempeño del algoritmo con grafos diversos se probara con 105, 205 y 1005 nodos
no_vertices = 205


ddn = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.uniform, 1, no_vertices-1 )
dw = InstanciesGenerator.Distribution(InstanciesGenerator.DistributionsTypes.normal, 15, 3)
generadorcon = InstanciesGenerator.GraphInstancesGenerator(graphtype = InstanciesGenerator.GraphTypes.connected,distribution_weight = dw,distribution_degree = ddn, directed = False )
#se probaran diferentes densidades del grafo para ver el desempeño cuando se va a acercando a la densidad de un grafo completo
density = [0.8,0.85,0.90,0.95]
replicas = 5
for d in density:
    gc = generadorcon.generateInstance('Test', no_vertices, round((no_vertices-1)*d*no_vertices))
    a = random.choice(gc.vertices)    
    for r in range(replicas):
    # se selccionan al azar 3 vertices para calcular el fluje en ellas
        b = random.choice(gc.vertices)
        while len(gc.vertices)>2 and b.id == a.id:
            b = random.choice(gc.vertices)
            # se calcua el flujo maximo entre los 2
        gc.resetflow()
        ti = time.clock()
        mf = gc.shortaugmentingmaxflow(a.id,b.id)
        tf = time.clock()-ti
        ti = time.clock()
        mb = gc.breadthfirstsearch(a.id)
        tfb = time.clock()-ti
        print(no_vertices,round((no_vertices-1)*d*no_vertices),r, mf, tf, tfb)

#se almacenaron los resultados en resultadosTarea5/result.pdf donde se ve que el algoritmo tarda mas cuando calcula mas flujo, (y que calculo mas caminos) o cuando aumenta la densidad del grafo. no se pudo contrastar contra el algoritmo de ford fulkerson que escoge un camino al azar ya que demoraba mucho mas tiempo para los experimentos.
