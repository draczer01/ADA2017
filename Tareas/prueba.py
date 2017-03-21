# from Ejercicios.turing import tupla_transicion, turing_machine
#
# MT = dict()
# MT["('s', '0')"] = tupla_transicion('s', '0', 'r')
# MT["('s', '1')"] = tupla_transicion('s', '1', 'r')
# MT["('s', '@')"] = tupla_transicion('t', '@', 'l')
# MT["('t', '1')"] = tupla_transicion('No', '1', 'o')
# MT["('t', '0')"] = tupla_transicion('Si', '0', 'o')
#
# stri = '01110@'
#
# tm = turing_machine(MT, stri)
# result = tm.strart()
# print(result)
# print(tm.current_state, tm.current_position)
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

g.add_edge(a, b, 7, True)
g.add_edge(a, c, 9, True)
g.add_edge(a, f, 14, True)
g.add_edge(b, c, 10, True)
g.add_edge(b, d, 15, True)
g.add_edge(c, d, 11, True)
g.add_edge('c', f, 2, True)
g.add_edge(d, e, 6, True)
g.add_edge(e, 'f', 9, True)

#print(g)
#g.
# print('end')
# k = lambda t, i: t[i]
#
# for r in g.vertices:
#     print(k(g, r))


#print(g)
#print( g.iscomplete)
#print( g.piscomplete())

#g = Tareas.graph.Graph('Grafo 2')
#a = Tareas.graph.Vertex('a', None)
#b = Tareas.graph.Vertex('b', None)
#b = Tareas.graph.Vertex('c', None)

#g.add_vertex(a)
#g.add_vertex(b)
#g.add_vertex(c)

#g.add_edge(a, b, 1)
#g.add_edge(a, c, 2)
#g.add_edge(b, c, 3)

print(g)
#print( g.iscomplete)
#print( g.piscomplete())
#g.deepfirstsearch(a)
g.bfirstsearch(a)


    # matr = g.adjacent_matrix()
    #
    # for i in matr:
    #     for j in matr[i]:
    #         print(i, j, matr[i][j])
