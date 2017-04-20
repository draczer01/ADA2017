import multiprocessing
import random
class Vertex:
    def __init__(self, _id, _object):
        self._id = _id
        self._value = _object
        self._outneighbors = {}
        self._inneighbors = {}


    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @property
    def neighbors(self):
        return self._outneighbors
    
    @property
    def inneighbors(self):
        return self._inneighbors
    def __str__(self):
        result = 'Vertex: ' + str(self.id) + '\n'
        result += 'Value: ' + str(self._value) + '\n'
        if any(self.neighbors):
            result += 'Neighbors: ('+ str(len(self.neighbors)) + ')\n'
            for n in self.neighbors:
                result += 'Vertex: ' + str(n) + ' weight: ' + str(self.neighbors[n])
                result += '\n'
        else:
            result += 'No Neighbors \n'
        
        if any(self.neighbors):
            result += 'In Neighbors: ('+ str(len(self.inneighbors)) + ')\n'
            for n in self.inneighbors:
                result += 'Vertex: ' + str(n) + ' weight: ' + str(self.inneighbors[n])
                result += '\n'
        else:
            result += 'No in Neighbors \n'
        return result

    def add_neighbor(self, _neighbor, _weight=1):
        self.neighbors[_neighbor] = _weight

    def add_inneighbor(self, _neighbor, _weight=1):
        self.inneighbors[_neighbor] = _weight

class Graph:
    def __init__(self, name, directed = False):
        self._vertices = dict()
        self._id = name
        self._directed = directed
        self._complete = None
        self._tree = None
        self.cyclic = None
        self._connect = None
    @property
    def vertices(self):
        return self._vertices

    @property
    def cardinal(self):
        return len(self._vertices)

    @property
    def id(self):
        return self._id

    @property
    def complete(self):
        if self._complete is None:
            self._complete = self.iscomplete()
        return self._complete

    @property
    def connected(self):
        if self._connect is None:
            self._connect = self.isconnected()
        return self._connect

    @property
    def tree(self):
        if self._tree is None:
            self._tree = self.istree()
        return self._tree

    @property
    def directed(self):
        return self._directed

    def __getitem__(self, item):
        res = None
        if isinstance(item, str):
            res = self._vertices[item]
            if res == None:
                res = [j for i, j in enumerate(self._vertices) if j.id == item]
        if isinstance(item, int):
            res = self._vertices[item]
        if isinstance(item, Vertex):
            res = [j for i, j in enumerate(self._vertices) if j == item]
        return res

    def __iter__(self):
        res = iter(self._vertices.values())
        return res

    def __str__(self):
        result = 'Graph: ' + str(self.id) + '\n'
        result += 'Number of vertices: ' + str(self.cardinal) + '\n'
        result += 'Number of edges: ' + str(self.getNumberEdges()) + '\n'
        result += 'Directed: ' + str(self.directed) +'\n'
        result += 'Connected: ' + str(self.connected) +'\n'
        result += 'Complete: ' + str(self.complete) +'\n'
        result += 'Tree: ' + str(self.tree) +'\n'
        for v in (self._vertices):
            result += str(self._vertices[v]) + '\n'
        return result

    def add_vertex(self, _vertex_obj):
        if isinstance(_vertex_obj, Vertex):
            if _vertex_obj not in self._vertices and _vertex_obj.id not in self._vertices.keys():
                self._vertices[_vertex_obj.id] = _vertex_obj
        return _vertex_obj

    def add_edge(self, _begin, _end, _weight=1):
#        beg, end = None, None
        if isinstance(_begin, Vertex):
            if _begin.id in self.vertices.keys():
                beg = self.vertices[_begin.id]
            else:
                beg = _beg
            self.add_vertex(beg)                
        else:
            if _begin in self._vertices.keys():
                beg = self._vertices[_begin]
            else:
                beg = Vertex(_begin, None)
                self.add_vertex(beg)
        if isinstance(_end, Vertex):
            if _end.id in self.vertices.keys():
                end = self.vertices[_end.id]
            else:
                end = _end
            self.add_vertex(end)
        else:
            if _end in self._vertices.keys():
                end = self._vertices[_end]
            else:
                end = Vertex(_end, None)
                self.add_vertex(end)

        # print(beg.id, end.id, _weight)
        if not self.directed:
            self.vertices[end.id].add_neighbor(beg.id, _weight)
            self.vertices[beg.id].add_inneighbor(end.id, _weight)
        self.vertices[beg.id].add_neighbor(end.id, _weight)
        self.vertices[end.id].add_inneighbor(beg.id, _weight)
#        print(beg.id, beg.inneighbors,end.id, end.inneighbors)

    def remove_vertex(self, v):
        if isinstance(v, Vertex):
            rem = v
        else:
            if v in self._vertices.keys():
                rem = self._vertices[v]
            else:
                return None
        result = Graph(self.id + ' -' + rem.id)
        for n in self._vertices:
            if rem .id != self._vertices[n]:
                a = Vertex(self._vertices[n].id, self._vertices[n].value)
                for nn in self._vertices[n].neighbors:
                    if nn != rem.id:
                        a.add_neighbor(nn, self._vertices[n].neighbors[nn])
                result.add_vertex(a)
        return result

    def have_leafs(self):
        result = False
        for v in self._vertices:
            if len(self._vertices[v].neighbors) == 0:
                result = True
                break
        else:
            result = False
        return result

    def adjacent_matrix(self):
        result = {}
        for v in self._vertices:
            result[v] = {}
            for n in self._vertices:
                if n in self._vertices[v].neighbors:
                    result[v][n] = self._vertices[v].neighbors[n]
                else:
                    result[v][n] = 0
        return result

    def vertexcomplete(self, v):
        result = False
        for n in self._vertices:
            if v != n and n not in self._vertices[v].neighbors:
                break
        else:
            result = True
        return result

    def iscomplete(self):
        result = True
        with multiprocessing.Pool() as pool:
            workers = []
            results = []
            for v in self._vertices:
                workers.append(pool.apply_async(func=Graph.vertexcomplete, args=(self, v,)))
            for w in workers:
                result = result and w.get()
        return result

    def istree(self):
        result = False
        if self.connected and (((self.getNumberEdges() if not self.directed else self.getNumberEdges()/2) -1) == self.cardinal):
            result = True
        return result

    def isconnected(self):
        result = False
        bfs = self.deepfirstsearch(None)
        if bfs.cardinal == self.cardinal:
            result = True
        return result

    def iscyclic(self):
        return False

    def getNumberEdges(self):
        edges = 0
        for v in self.vertices:
                edges+= len(self._vertices[v].neighbors)
        return edges

    def deepfirstsearch(self, v):
        if not v or v is None:
            v = self[random.choice(list(self.vertices))]
        g = Graph('DFS: ' + self.id)
        g.add_vertex(Vertex(v.id, v.value))
        p = [v]
        l = set()
        while len(p)>0:
            av = p[-1]
            l.add(av.id)
            # print(av.id)
            if len(av.neighbors) > 0:
                cl = list(set(av.neighbors)-l)
                if len(cl) > 0:
                    dv = random.choice(cl)
                    p.append(self[dv])
                    g.add_edge(Vertex(av.id, av.value),Vertex(dv,self[dv].value), len(p)-1)
                    continue
            p.pop()
        return g

    def breadthfirstsearch(self, v):
        if not v or v is None:
            v = self[random.choice(list(self.vertices))]
        g = Graph('BFS: ' + self.id)
        g.add_vertex(Vertex(v.id, v.value))
        levels = {v.id: 0}
        sig = [v]
        print(v.id, levels[v.id])
        while len(sig) > 0:
            mark = []
            for l in sig:
                for n in l.neighbors:   
                    if n not in levels:
                        print('l:',levels)
                        print(n, levels[l.id])
                        levels[n]= levels[l.id]+1
                        mark.append(self[n])
                        g.add_edge(l.id, Vertex(n, self[n].value), levels[n])
            sig = mark            
        return g
                    
