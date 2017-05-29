# clase grafo

import files.graph
import graph

g = graph.Graph('Grafo 1')
a = graph.Vertex('a', None)
b = graph.Vertex('b', None)
c = graph.Vertex('c', None)
d = graph.Vertex('d', None)
e = graph.Vertex('e', None)
f = graph.Vertex('f', None)
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_vertex(f)

g.add_edge(a, b, 7)
g.add_edge(a, c, 9)
g.add_edge(a, f, 14)
g.add_edge(b, c, 10)
g.add_edge(b, d, 15)
g.add_edge(c, d, 11)
g.add_edge('c', f, 2)
g.add_edge(d, e, 6)
g.add_edge(e, 'f', 9)

print(g)
