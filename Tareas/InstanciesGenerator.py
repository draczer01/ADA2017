import graph
import random
from enum import Enum

class GraphTypes(Enum):
    complete = 0
    connected = 1
    tree = 2

    
class DistributionsTypes(Enum):
    uniform = 1
    normal = 2
    exponential = 3
    random = 10

class Distribution():
    def __init__(self, Distribution_type = DistributionsTypes.uniform, p1 = None, p2 = None):
        self.type = Distribution_type
        self._parameter1 = p1
        self._parameter2 = p2

    @property
    def parameter1(self):
        return self._parameter1
    
    @property
    def parameter2(self):
        return self._parameter2

class GraphInstancesGenerator():
    def __init__(self, graphtype, distribution_weight, distribution_degree, directed = True):
        self.directed = directed
        self.type = graphtype
        if self.type is GraphTypes.complete:
            self.distributiondegree = Distribution(DistributionsTypes.uniform, 10)
        else:
            self.distributiondegree = distribution_degree
        self.distributionweight = distribution_weight
        

    def generateInstance(self, name, novertex, noedges):
        g = graph.Graph(name, self.directed)
        if self.type is GraphTypes.complete:
            #Generador de grafos completos
            if self.directed:
                noedges = novertex*(novertex-1)
            else:
                noedges = (novertex*(novertex-1))/2
            for i in range(novertex):
                #self.distributiondegree = DistributionsTypes.uniform                
                for j in range(i+1,novertex):                        
                    weight = 1
                    if self.distributionweight.type is DistributionsTypes.uniform:
                        weight = self.distributionweight.parameter1
                    if self.distributionweight.type is DistributionsTypes.normal:
                        weight = round(random.normalvariate(self.distributionweight.parameter1,self.distributionweight.parameter2))
                    if self.distributionweight.type is DistributionsTypes.exponential:
                        weight = round(random.expvariate(1/(self.distributionweight.parameter1)))
                    g.add_edge(i,j,weight)
        if self.type is GraphTypes.tree:
            #Generador de arboles
            noedges = novertex-1
            for i in range(novertex):
               nv = graph.Vertex(i, None)
               g.add_vertex(nv)
                
            av = random.choice(g.vertices)
            available = (set(g.vertices) - {av.id})
            while av:
                if self.distributiondegree.type is DistributionsTypes.uniform:
                    degree = self.distributiondegree.parameter1
                if self.distributiondegree.type is DistributionsTypes.normal:
                    degree = round(random.normalvariate(self.distributionweight.parameter1,self.distributionweight.parameter2))
                if self.distributiondegree.type is DistributionsTypes.exponential:
                    degree = round(random.expvariate(1/(self.distributionweight.parameter1)))
                for i in range(degree):
                    if len(available)<1:
                        break                        
                    ia = [x for x in available]# if len(g[x].neighbors) == 0]
                    print(ia)
                    print([x for x in ia if len(g[x].neighbors) == 0 ])# if len(g[x].neighbors) == 0]]
                    if len(ia) > 0:
                        nv = random.choice(ia)
                    weight = 1
                    if self.distributionweight.type is DistributionsTypes.uniform:
                        weight = self.distributionweight.parameter1
                    if self.distributionweight.type is DistributionsTypes.normal:
                        weight = round(random.normalvariate(self.distributionweight.parameter1,self.distributionweight.parameter2))
                    if self.distributionweight.type is DistributionsTypes.exponential:
                        weight = round(random.expvariate(1/(self.distributionweight.parameter1)))
                    g.add_edge(av,nv,weight)
                    available-= {nv}
                if len(available) > 0 :
                    av = g[random.choice(list())]
                else:
                    av = None
                    break
                                    
                
        return g
               
