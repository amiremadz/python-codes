#!/usr/bin/python3

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited_ordered = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            visited_ordered.append(node)
            queue.extend(graph[node] - visited)
    
    return visited_ordered

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        for nxt in graph[node] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def dfs_itr(graph, start):
    visited = set()
    stack = [start]
    visited_ordered = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            visited_ordered.append(node)
            stack.extend(graph[node] - visited)

    return visited_ordered

def dfs_rec(graph, start, visited=None, visited_ordered=None):
    if visited == None:
        visited = set()
    if visited_ordered == None:
        visited_ordered = []

    visited.add(start)
    visited_ordered.append(start)

    for nbr in (graph[start] - visited):
        dfs_rec(graph, nbr, visited, visited_ordered)
    return visited_ordered

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        for nxt in graph[node] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

if __name__ == "__main__":
    #graph = {'A': set(['B', 'C']),
    #        'B': set(['A', 'D', 'E']),
    #        'C': set(['A', 'F']),
    #        'D': set(['B']),
    #        'E': set(['B', 'F']),
    #        'F': set(['C', 'E'])}
    
    graph = {'A': set(['B', 'C']),
            'B': set(['D', 'E']),
            'C': set(['F']),
            'D': set(),
            'E': set(['F']),
            'F': set()}

    print(bfs(graph, 'A'))
    print(list(bfs_paths(graph, 'A', 'F')))
    print(shortest_path(graph, 'A', 'F'))
    print("\n")
    print(dfs_itr(graph, 'A'))
    print(dfs_rec(graph, 'A'))
    print(list(dfs_paths(graph, 'A', 'F')))
