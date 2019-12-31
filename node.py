up = 1
down = 2
left = 3
right = 4

class Node:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.isStart = False
        self.isEnd = False
        self.up = ()
        self.down = ()
        self.left = ()
        self.right = ()
        self.number = number
        self.visited = False
    
    def connect(self, node, distance, direction):
        if (direction == up):
            if (self.up == ()):
                self.up = (node, distance)
        elif (direction == down):
            if (self.down == ()):
                self.down = (node, distance)
        elif (direction == left):
            if (self.left == ()):
                self.left = (node, distance)
        elif (direction == right):
            if (self.right == ()):
                self.right = (node, distance)
    
    def Start(self):
        self.isStart = True
    
    def End(self):
        self.isEnd = True
    
    def visit(self):
        self.visited = not self.visited