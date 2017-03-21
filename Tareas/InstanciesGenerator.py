import Tareas.graph
import random

def graphInstanciesGenerator(name, novertex, noedges, weightp1, weightp2, Type = 'conected', directed = False, distributionweight = 'uniform', distributionedges= 'uniform'):
    g = Tareas.graph.Graph(name)
    completeedges = novertex*novertex-1//2
    if(completeedges < novertex):
        noedges = completeedges
    for i in range(novertex):
        g.add_vertex(Tareas.graph.Vertex(str(i), None))
    for e in range(noedges):
        if (distributionedges == 'uniform'):
            """generador de valores deacuerdo a la distribucion"""
            select = False
            la = list(g.vertices)
            while not select:
                a = random.choice(la)
                b = random.choice(la-list(g[a].neighbors)-a)
                if b != a:
                    select = True
        if (distributionweight == 'uniform'):
            w = random.randint(weightp1, weightp2)
        va = g[a]
        vb = g[b]
        print(e, a, b, w)
        g.add_edge(va, vb, w, directed)
    return g
