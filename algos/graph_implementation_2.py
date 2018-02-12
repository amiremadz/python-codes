#!/usr/bin/python

from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited  = 1
    visited    = 2
    visiting   = 3

class Node:
    def __init__(self, key):
        self.id = key
        self.status = State.unvisited
        self.adjacent = OrderedDict()

    def add_nbr(self, nbr, weight=0):
        self.adjacent[nbr] = weight

    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self):
        self.nodes_list = OrderedDict()
        
    def add_node(self, key):
        node = Node(key)
        self.nodes_list[key] = node

    def add_edge(self, fr, to, weight=0):
        if fr not in self.nodes_list.keys():
            self.add_node(fr)
        if to not in self.nodes_list.keys():
            self.add_node(to)
        self.nodes_list[fr].add_nbr(self.nodes_list[to], weight)

    def __iter__(self):
        return iter(self.nodes_list.values())


if __name__ == "__main__":
    g = Graph()

    for i in range(6):
        g.add_node(i)

    g.add_edge(0, 1, 22)
    g.add_edge(0, 2, 33)
    print(g.nodes_list)
    print("\n")

    g.add_edge(5, 6, 44)
    print(g.nodes_list)
    print("\n")

    for vertex in g:
        print(vertex)
        print(str(vertex.adjacent.keys()) + ": " + str(vertex.adjacent.values()))
        print("\n")
