class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isStart = False
        self.isEnd = False
        self.connected = []
    
    def connect(self, node):
        self.connected.append(node)
    
    def Start(self):
        self.isStart = True
    
    def End(self):
        self.isEnd = True