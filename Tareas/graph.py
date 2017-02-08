import multiprocessing
class Vertex:
    def __init__(self, _id, _object):
        self._id = _id
        self._value = _object
        self._neighbors = {}

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @property
    def neighbors(self):
        return self._neighbors

    def __str__(self):
        result = 'Vertex: ' + str(self.id) + '\n'
        result += 'Value: ' + str(self._value) + '\n'
        if any(self._neighbors):
            result += 'Neighbors: \n'
            for n in self._neighbors:
                result += 'Vertex: ' + str(n) + ' weight: ' + str(self._neighbors[n])
                result += '\n'
        else:
            result += 'No Neighbors \n'
        return result

    def add_neighbor(self, _neighbor, _weight=1):
        self._neighbors[_neighbor] = _weight

class Graph:
    def __init__(self, name):
        self._vertexs = dict()
        self._cardinal = 0
        self._id = name
    @property
    def vertexs(self):
        return self._vertexs

    @property
    def cardinal(self):
        return self._cardinal

    @property
    def id(self):
        return self._id

    def __getitem__(self, item):
        res = None
        if isinstance(item, str):
            res = self._vertexs[item]
            if res == None:
                res = [j for i, j in enumerate(self._vertexs) if j.id == item]
        if isinstance(item, int):
            res = self._vertexs[item]
        if isinstance(item, Vertex):
            res = [j for i, j in enumerate(self._vertexs) if j == item]
        return res

    def __iter__(self):
        res = iter(self._vertexs.values())
        return res

    def __str__(self):
        result = 'Graph: ' + str(self.id) + '\n'
        result += 'Number of vertexs: ' + str(self._cardinal) + '\n'
        for v in (self._vertexs):
            result += str(self._vertexs[v]) + '\n'
        return result

    def add_vertex(self, _vertex_obj):
        if isinstance(_vertex_obj, Vertex):
            if _vertex_obj not in self._vertexs and _vertex_obj.id not in self._vertexs.keys():
                self._vertexs[_vertex_obj.id] = _vertex_obj
                self._cardinal += 1
        return _vertex_obj

    def add_edge(self, _begin, _end, _weight=1, directed=False):
        if isinstance(_begin, Vertex):
            beg = _begin
            self.add_vertex(beg)
        else:
            if _begin in self._vertexs.keys():
                beg = self._vertexs[_begin]
        if isinstance(_end, Vertex):
            end = _end
            self.add_vertex(end)
        else:
            if _end in self._vertexs.keys():
                end = self._vertexs[_end]

        if not directed:
            self._vertexs[end.id].add_neighbor(beg.id, _weight)
        self._vertexs[beg.id].add_neighbor(end.id, _weight)

    def remove_vertex(self, v):
        if isinstance(v, Vertex):
            rem = v
        else:
            if v in self._vertexs.keys():
                rem = self._vertexs[v]
            else:
                return None
        result = Graph(self.id + ' -' + rem.id)
        for n in self._vertexs:
            if rem .id != self._vertexs[n]:
                a = Vertex(self._vertexs[n].id, self._vertexs[n].value)
                for nn in self._vertexs[n].neighbors:
                    if nn != rem.id:
                        a.add_neighbor(nn, self._vertexs[n].neighbors[nn])
                result.add_vertex(a)
        return result

    def have_leafs(self):
        for v in self.__vertexa

    def adjacent_matrix(self):
        result = {}
        for v in self._vertexs:
            result[v] = {}
            for n in self._vertexs:
                if n in self._vertexs[v].neighbors:
                    result[v][n] = self._vertexs[v].neighbors[n]
                else:
                    result[v][n] = 0
        return result

    def vertexcomplete(self, v):
        result = False
        for n in self._vertexs:
            if v != n and n not in self._vertexs[v].neighbors:
                break
        else:
            result = True
        return result

    @property
    # def iscomplete(self):
    #
    #     result = False
    #     for v in self._vertexs:
    #         if not self.vertexcomplete(v):
    #             break
    #     else:
    #         result = True
    #     return result
    def iscomplete(self):
        result = True
        with multiprocessing.Pool() as pool:
            workers = []
            results = []
            for v in self._vertexs:
                workers.append(pool.apply_async(func=Graph.vertexcomplete, args=(self, v,)))
            for w in workers:
                result = result and w.get()
        return result

    def iscyclic(self):

        return False

    def dijska(self, a, b):
        result = {}
        """ TODO: algoritmo dijska"""
        if isinstance(a, str):
            vi = self._vertexs[a]
        if isinstance(a, Vertex):
            vi = self._vertexs[a.id]
        if isinstance(b, str):
            vf = self._vertexs[b]
        if isinstance(b, Vertex):
            vf = self._vertexs[b.id]
        if vi == vf:
            result[0] = vf
        if net.has_key(s) == False:
            return "There is no start node called " + str(s) + "."
        if net.has_key(t) == False:
            return "There is no terminal node called " + str(t) + "." 
        distances = dict()
        path = dict()


