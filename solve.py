from node import Node
from data import *

dfs = 1
bfs = 2
dstr = 3
astar = 4

def solve(maze, algorithm):
    path = []
    if (algorithm == dfs):
        path = depthFirstSearch(maze.nodes, 0)
    elif (algorithm == bfs):
        path = breadtFirstSearch(maze.nodes, 0)
    elif (algorithm == dstr):
        path = dijkstra(maze.nodes, 0)
    elif (algorithm == astar):
        path = aStar(maze.nodes, 0)
    return path

def depthFirstSearch(nodes, start):
    stack = Stack()
    stack.push((start, [start]))
    visited = set()
    while stack:
        (node, path) = stack.pop()
        if (node not in visited):
            if (nodes[node].isEnd):
                return path
            visited.add(node)
            for i in getNeighbours(nodes, node):
                stack.push((i, path + [i]))

def getNeighbours(nodes, node):
    neighbours = []
    if (nodes[node].up != ()):
        neighbours.append(nodes[node].up[0].number)
    if (nodes[node].down != ()):
        neighbours.append(nodes[node].down[0].number)
    if (nodes[node].left != ()):
        neighbours.append(nodes[node].left[0].number)
    if (nodes[node].right != ()):
        neighbours.append(nodes[node].right[0].number)
    return neighbours

def breadtFirstSearch(nodes, node):
    pass

def dijkstra(nodes, node):
    pass

def aStar(nodes, node):
    pass