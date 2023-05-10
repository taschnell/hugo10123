#!/usr/bin/env python3
'''
Graph Data Type Module for Python
'''
from collections import defaultdict

#problem regarding the missing method, need to add vertex when calling __setitem__


class Graph(defaultdict):
    
    def __missing__(self, vertex):
        print(vertex in self)
        if vertex not in self:
            super().__setitem__(vertex, {})
        print(vertex in self)
        return super().__getitem__(vertex)

    def __setitem__(self, dst, weight):
        super().__getitem__(dst)
        print(dst)

        return super().__setitem__(dst, weight)
    
    def vertices(self):
        vertex_set = set()
        for vertex in self:
            vertex_set.add(vertex)
        return vertex_set

    def __len__(self):
        return len(self.vertices())    

    def __delitem__(self, __key) -> None:
        return super().__delitem__(__key)
    

g = Graph()
print(g)



print(g)

g["a"]["z"] = 10
print(g)
g["a"]['B'] = 5
print(g)


print(g.vertices())
print(g)
del g["a"]["z"]
print(g)