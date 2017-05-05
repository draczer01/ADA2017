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

    def getweightvalue(self):
        weight = 1
        if self.distributionweight.type is DistributionsTypes.uniform:
            if  self.distributionweight.parameter2 is not None:
                weight = random.randint(self.distributionweight.parameter1, self.distributionweight.parameter2)
            else:
                weight = self.distributionweight.parameter1
        if self.distributionweight.type is DistributionsTypes.normal:
            weight = round(random.normalvariate(self.distributionweight.parameter1,self.distributionweight.parameter2))
        if self.distributionweight.type is DistributionsTypes.exponential:
            weight = round(random.expvariate(1/(self.distributionweight.parameter1)))
        return weight

    
    def getdegreevalue(self, noedges, novertex):
        degree = 1
        if self.distributionweight.type is DistributionsTypes.uniform:
            if  self.distributionweight.parameter2 is not None:
                degree = random.randint(self.distributionweight.parameter1, min(self.distributionweight.parameter2, novertex))
            else:
                degree = min(self.distributionweight.parameter1, novertex)
        if self.distributiondegree.type is DistributionsTypes.normal:
            degree = round(random.normalvariate(self.distributiondegree.parameter1,self.distributiondegree.parameter2))
            degree = min(degree, novertex)
        if self.distributiondegree.type is DistributionsTypes.exponential:
            degree = round(random.expvariate(1/(self.distributiondegree.parameter1)))
            degree = min(degree, novertex)
        return degree

   
    def generateTree(self, name, novertex):
        g = graph.Graph(name, self.directed)
        #Generador de arboles
        noedges = novertex-1
        for i in range(novertex):
            nv = graph.Vertex(i, None)
            g.add_vertex(nv)          
        available = list(g.vertices)
        random.shuffle(available)      
        ne = 0
        leaf = []
        iav = available.pop()
        av = g[iav]
        while ne < noedges:
            degree = self.getdegreevalue(noedges, novertex)
            for i in range(degree):
                # if connected 
                if len(available) < 1 or ne >= noedges:
                    break                        
                inv =  available.pop()
                nv = g[inv]
                weight = self.getweightvalue()
                g.add_edge(av,nv,weight)
                leaf.append(inv)
                ne+=1
            if len(leaf) > 0 :
                iav = random.choice(leaf)
                av = g[iav]
                leaf.remove(iav)
            else:
                av = None
                break
        return g

    def generateConected(self,name, novertex, noedges):
        if noedges > novertex -1:
            g = self.generateTree(name, novertex)
            vl = list(g.vertices)
            for n in range(novertex, noedges):
                
            
    
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
                    weight = self.getweightvalue()
                    g.add_edge(i,j,weight)
        if self.type is GraphTypes.tree:
            #Generador de arboles
            g = self.generateTree(name, novertex)
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
                degree = self.getdegreevalue(noedges, novertex)
                actneigh = []
                for i in range(degree):
                    availableneigh = [x for x in g.vertices if x != av.id and x not in actneigh]                    
                    # if connected 
                    if len(availableneigh) < 1 or ne >= noedges:
                        break                                              
                    inv = random.choice(availableneigh)
                    nv = g[inv]
                    weight = self.getweightvalue()
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
               
