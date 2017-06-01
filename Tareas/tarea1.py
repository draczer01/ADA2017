# clase grafo
from files import graph

g = graph.Graph('Grafo 1', True)
a = graph.Vertex('a', object=None)
b = graph.Vertex('b', coord=(1,2))
c = graph.Vertex('c')
d = graph.Vertex('d')
e = graph.Vertex('e')
f = graph.Vertex('f')
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_vertex(f)

g.add_edge(a, b, weight=7, capacity=10)
g.add_edge(a, c, weight=9, capacity=18)
g.add_edge(a, f, weight=14, capacity=20)
g.add_edge(b, c, weight=10, capacity = 15, unitary_cost=2)
g.add_edge(b, d, weight=15, capacity=17)
g.add_edge(c, d, weight=11, capacity=14)
g.add_edge('c', f, weight=2, capacity=13)
g.add_edge(d, e, weight=6, capacity=9)
g.add_edge(e, 'f', weight=9, capacity=11)
g.add_edge('a', 'e', weight=3, capacity=5)



mf = g.maxflow('a','e')
print(g)
print(mf)
print(g.shortest('a','e', key='weight'))


