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
            availableroot = [x for x in g.vertices if x != av.id ]
            ne = 0
            used = {av.id}
            #while av and len(available)>0:
            while ne < noedges:
                if self.distributiondegree.type is DistributionsTypes.uniform:
                    degree = round(noedges/novertex)*self.distributiondegree.parameter1
                if self.distributiondegree.type is DistributionsTypes.normal:
                    degree = round(random.normalvariate(self.distributiondegree.parameter1,self.distributiondegree.parameter2))
                if self.distributiondegree.type is DistributionsTypes.exponential:
                    degree = round(random.expvariate(1/(self.distributiondegree.parameter1)))
                for i in range(degree):
                    availableneigh = [x for x in g.vertices if x not in used and len(g[x].neighbors) == 0 and len(g[x].inneighbors) == 0 ]                    
                    # if connected 
                    if len(availableneigh) < 1 or ne >= noedges:
                        break                        
                    inv = random.choice(availableneigh)
                    nv = g[inv]
                    weight = 1
                    if self.distributionweight.type is DistributionsTypes.uniform:
                        weight = self.distributionweight.parameter1
                    if self.distributionweight.type is DistributionsTypes.normal:
                        weight = round(random.normalvariate(self.distributionweight.parameter1,self.distributionweight.parameter2))
                    if self.distributionweight.type is DistributionsTypes.exponential:
                        weight = round(random.expvariate(1/(self.distributionweight.parameter1)))
                    g.add_edge(av,nv,weight)
                    ne+=1
                    #if connected and tree
                #if connected
                availableroot = [x for x in g.vertices if x not in used and len(g[x].inneighbors) > 0 ]
                if len(availableroot) > 0 :
                    iav = random.choice(availableroot)
                    av = g[iav]
                    used.add(av.id)
                else:
                    av = None
                    break
        if self.type is GraphTypes.connected:
            #Generador de grafos pseudo connectados
            for i in range(novertex):
               nv = graph.Vertex(i, None)
               g.add_vertex(nv)                
            av = random.choice(g.vertices)
            availableroot = [x for x in g.vertices if x != av.id ]
            ne = 0
            used = {av.id}
            #while av and len(available)>0:
            while ne < noedges:
                if self.distributiondegree.type is DistributionsTypes.uniform:
                    degree = round(noedges/novertex)*self.distributiondegree.parameter1
                if self.distributiondegree.type is DistributionsTypes.normal:
                    degree = round(random.normalvariate(self.distributiondegree.parameter1,self.distributiondegree.parameter2))
                if self.distributiondegree.type is DistributionsTypes.exponential:
                    degree = round(random.expvariate(1/(self.distributiondegree.parameter1)))
                actneigh = []
                for i in range(degree):
                    availableneigh = [x for x in g.vertices if x != av.id and x not in actneigh]                    
                    # if connected 
                    if len(availableneigh) < 1 or ne >= noedges:
                        break                                              
                    inv = random.choice(availableneigh)
                    nv = g[inv]
                    weight = 1
                    if self.distributionweight.type is DistributionsTypes.uniform:
                        weight = self.distributionweight.parameter1
                    if self.distributionweight.type is DistributionsTypes.normal:
                        weight = round(random.normalvariate(self.distributionweight.parameter1,self.distributionweight.parameter2))
                    if self.distributionweight.type is DistributionsTypes.exponential:
                        weight = round(random.expvariate(1/(self.distributionweight.parameter1)))
                    g.add_edge(av,nv,weight)
                    actneigh.append(inv)
                    ne+=1
                #if connected
                availableroot = [x for x in g.vertices if x not in used and len(g[x].inneighbors) > 0 ]
                if len(availableroot) > 0 :                      
                    iav = random.choice(availableroot)
                    av = g[iav]
                    used.add(iav)
                else:
                    av = None
                    break                
        return g
               
