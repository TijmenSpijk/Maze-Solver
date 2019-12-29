class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected = []
    
    def connect(self, node):
        self.connected.append(node)