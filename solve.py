from node import Node
from data import Stack, Queue

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
            for neighbour in getNeighbours(nodes, node):
                stack.push((neighbour, path + [neighbour]))

def breadtFirstSearch(nodes, start):
    queue = Queue()
    queue.enqueue((start, [start]))
    visited = set()
    visited.add(start)
    while queue:
        (node, path) = queue.dequeue()
        if (nodes[node].isEnd):
            return path
        for neighbour in getNeighbours(nodes, node):
            if (neighbour not in visited):
                visited.add(neighbour)
                queue.enqueue((neighbour, path + [neighbour]))

def dijkstra(nodes, start):
    pass

def aStar(nodes, start):
    pass

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