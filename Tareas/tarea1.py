#archivos necesarios dentro de la carpeta files
# graph.py

# clase grafo
from files import graph
#Crear grafo
g = graph.Graph('Grafo 1', True)
#Crear vertices con diferentes tipos de etiquetas
a = graph.Vertex('a', object=None)
b = graph.Vertex('b', coord=(1,2))
c = graph.Vertex('c', costo = 15)
d = graph.Vertex('d', object= None, coord=(3,1))
e = graph.Vertex('e')
f = graph.Vertex('f')
#Insertar vertices en el grafo
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_vertex(f)
#Insertar aristas en el grafo, con diferentes etiquetas
g.add_edge(a, b, weight=7, capacity=10)
g.add_edge(a, c, weight=9, capacity=18)
g.add_edge(a, f, weight=14, capacity=20)
g.add_edge(b, c, weight=10, capacity = 15, unitary_cost=2)
g.add_edge(b, d, weight=15, capacity=17)
g.add_edge(c, d, weight=11, capacity=14)
g.add_edge('c', f, weight=2, capacity=13)
g.add_edge(d, e, weight=1, capacity=9)
g.add_edge(e, 'f', weight=9, capacity=11)
g.add_edge('a', 'e', weight=35, capacity=5)
#Maximo Flujo de a a e
mf = g.maxflow('a','e')
g.connected
g.complete
g.tree

#imprimir grafo
print(g.to_string())
#DFS
print('DFS: ',g.deepfirstsearch('a'))
#BFS
print('BFS: ',g.breadthfirstsearch('a'))
#Imprimirel Max Flujo de a -> e
print('MF: ',mf)
#camino mas corto de a -> e deacuerdo al peso
print('WSP: ',g.shortest('a','e', key='weight'))
#camino mas corto de a -> e deacuerdo al numero de aristas
print('ESP: ',g.shortest('a','e', key='edge'))
#arbol de expansion minima
print('MST: ',g.kruskal().to_string())
#valor de centralidad media
print('BC: ',g.betweennesscentrality())
#valor de centralidad de cercania
print('CC: ',g.closenesscentrality())




