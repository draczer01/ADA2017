from graph import Graph, Vertex

g = Graph('Grafo 1')
a = Vertex('a', None)
b = Vertex('b', None)
c = Vertex('c', None)
d = Vertex('d', None)
e = Vertex('e', None)
f = Vertex('f', None)
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_vertex(f)

g.add_edge(a, b, 7, True)
g.add_edge(a, c, 9, True)
g.add_edge(a, f, 14, True)
g.add_edge(b, c, 10, True)
g.add_edge(b, d, 15, True)
g.add_edge(c, d, 11, True)
g.add_edge('c', f, 2, True)
g.add_edge(d, e, 6, True)
g.add_edge(e, 'f', 9, True)

print(g)

# print('end')
# k = lambda t, i: t[i]
#
# for r in g.vertexs:
#     print(k(g, r))


print(g)
print( g.iscomplete)
print( g.piscomplete())

g = Graph('Grafo 2')
a = Vertex('a', None)
b = Vertex('b', None)
b = Vertex('c', None)

g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)

g.add_edge(a, b, 1)
g.add_edge(a, c, 2)
g.add_edge(b, c, 3)

print(g)
print( g.iscomplete)
print( g.piscomplete())


    # matr = g.adjacent_matrix()
    #
    # for i in matr:
    #     for j in matr[i]:
    #         print(i, j, matr[i][j])
