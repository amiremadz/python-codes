#!/usr/bin/python

class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    # Node type: weight
    def add_nbr(self, nbr, weight = 0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]
    
    def __str__(self):
        return str(self.id) + " connected to: " + str([ nbr.id for nbr in self.connected_to]) + "\n"

class Graph:
    def __init__(self):
        self.node_list = {}
        self.num_nodes = 0

    def add_node(self, key):
        self.num_nodes += 1
        node = Node(key)
        self.node_list[key] = node

    def get_node(self, key):
        if key in self.node_list:
            return self.node_list[key] 
        else:
            return None

    def add_edge(self, fr, to, weight=0):
        if fr not in self.node_list.keys():
            self.add_node(fr)
        if to not in self.node_list.keys():
            self.add_node(to)

        self.node_list[fr].add_nbr(self.node_list[to], weight)

    def get_nodes(self):
        return self.node_list.keys()

    def __contains__(self, key):
        return key in self.node_list

    def __iter__(self):
        return iter(self.node_list.values())

    def __str__(self):
        return str(self.node_list)

if __name__ == "__main__":
    g = Graph()

    for i in range(6):
        g.add_node(i)

    print(g)

    g.add_edge(0, 1, 20)

    for vertex in g:
        print(vertex)
        print(vertex.get_connections())
        print("\n")

    if 6 in g:
        print("True")
    else:
        print("False")
