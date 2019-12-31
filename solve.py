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

def depthFirstSearch(nodes, node):
    path = []
    if (nodes[node].isEnd):
        return [node]
    nodes[node].visit()
    if ((nodes[node].up != ()) and (not nodes[node].up[0].visited)):
        path.extend(depthFirstSearch(nodes, nodes[node].up[0].number))
        path.insert(0, node)
        if (nodes[path[path.count(path) - 1]].isEnd):
            return path
    if ((nodes[node].down != ()) and (not nodes[node].down[0].visited)):
        path.extend(depthFirstSearch(nodes, nodes[node].down[0].number))
        path.insert(0, node)
        if (nodes[path[path.count(path) - 1]].isEnd):
            return path
    if ((nodes[node].left != ()) and (not nodes[node].left[0].visited)):
        path.extend(depthFirstSearch(nodes, nodes[node].left[0].number))
        path.insert(0, node)
        if (nodes[path[path.count(path) - 1]].isEnd):
            return path
    if ((nodes[node].right != ()) and (not nodes[node].right[0].visited)):
        path.extend(depthFirstSearch(nodes, nodes[node].right[0].number))
        path.insert(0, node)
        if (nodes[path[path.count(path) - 1]].isEnd):
            return path
    return path

def breadtFirstSearch(nodes, node):
    pass

def dijkstra(nodes, node):
    pass

def aStar(nodes, node):
    pass