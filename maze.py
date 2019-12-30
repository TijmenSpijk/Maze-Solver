from PIL  import Image
from node import Node
#some global colors
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red   = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue  = (0, 0, 255, 255)

#some global directions
up = 1
down = 2
left = 3
right = 4

# {
#   The Maze Class:
#   The class to convert the image into a maze
#   The maze is defined by a set of connected nodes
# }
class Maze:
    def __init__(self, image: Image):
        self.image = image
        self.imageNodes = image.copy()
        self.imagePath = image.copy()
        self.width = image.width
        self.height = image.height
        self.nodes = []
        self.createNodes()
        self.connectNodes()

    # Function to conver the image into a set of connected nodes
    def createNodes(self):
        xstart, ystart = self.findStart(), 1
        start = Node(xstart, ystart)
        start.Start()
        self.nodes.append(start)
        # check all pixel => check if that pixel needs to be a node
        for i in range(1, self.width - 1):
            for j in range(2, self.height - 1):
                pixel = self.image.getpixel((i, j))
                if (pixel == white):
                    # Corner
                    if (self.isCorner(i, j)):
                        node = Node(i, j)
                        self.nodes.append(node)
                    # T-Spit
                    elif (self.isTSplit(i, j)):
                        node = Node(i, j)
                        self.nodes.append(node)
                    # Dead End
                    elif (self.isDeadEnd(i, j)):
                        node = Node(i, j)
                        self.nodes.append(node)
                    # Cross Road
                    elif (self.isCrossroad(i, j)):
                        node = Node(i, j)
                        self.nodes.append(node)
        xend, yend = self.findEnd(), self.width - 2
        end = Node(xend, yend)
        end.End()
        self.nodes.append(end)

# region => Find Nodes
    # Funtion to find the start node of the maze
    def findStart(self):
        for i in range(1, self.width - 1):
            if (self.image.getpixel((i, 1)) == white):
                return i
        return None

    # Function to find the end node of the maze
    def findEnd(self):
        for i in range(1, self.width - 1):
            if (self.image.getpixel((i, self.height - 2)) == white):
                return i
        return None

    # Function to check if a certain pixel is a corner of the maze
    def isCorner(self, x, y):
        # get neighbouring pixel
        up = self.image.getpixel((x,y-1))
        down = self.image.getpixel((x,y+1))
        left = self.image.getpixel((x-1,y))
        right = self.image.getpixel((x+1,y))
        # corner criteria
        if (up == black and right == black and left == white and down == white):
            return True
        elif (up == white and right == black and left == white and down == black):
            return True
        elif (up == white and right == white and left == black and down == black):
            return True
        elif (up == black and right == white and left == black and down == white):
            return True
        return False

    # Function to chek if a certain pixel is a t-split in the maze
    def isTSplit(self, x, y):
        up = self.image.getpixel((x,y-1))
        down = self.image.getpixel((x,y+1))
        left = self.image.getpixel((x-1,y))
        right = self.image.getpixel((x+1,y))
        # tsplit criteria
        if (up == black and right == white and left == white and down == white):
            return True
        elif (up == white and right == black and left == white and down == white):
            return True
        elif (up == white and right == white and left == black and down == white):
            return True
        elif (up == white and right == white and left == white and down == black):
            return True
        return False

    # Funtion to check if a certain pixel is a dead-end in the maze
    def isDeadEnd(self, x, y):
        up = self.image.getpixel((x,y-1))
        down = self.image.getpixel((x,y+1))
        left = self.image.getpixel((x-1,y))
        right = self.image.getpixel((x+1,y))
        if (up == white and right == black and left == black and down == black):
            return True
        elif (up == black and right == white and left == black and down == black):
            return True
        elif (up == black and right == black and left == white and down == black):
            return True
        elif (up == black and right == black and left == black and down == white):
            return True
        return False
    
    def isCrossroad(self, x, y):
        up = self.image.getpixel((x,y-1))
        down = self.image.getpixel((x,y+1))
        left = self.image.getpixel((x-1,y))
        right = self.image.getpixel((x+1,y))
        if (up == white and right == white and left == white and down == white):
            print("found one")
            return True
        return False
# endregion

# region => Connect Nodes
    # Function to connect neighbouring nodes
    def connectNodes(self):        
        for node in self.nodes:
            neighbours = 0
            for restnode in self.nodes:
                if (node.x == restnode.x and node.y != restnode.y):
                    if (self.checkWallY(node.y, restnode.y, node.x)):
                        distance = abs(node.x - restnode.x)
                        if (node.y > restnode.y): d1, d2 = up, down
                        else: d1, d2 = down, up
                        node.connect(restnode, distance, d1)
                        restnode.connect(node, distance, d2)
                        neighbours += 1
                elif (node.y == restnode.y and node.x != restnode.x):
                    if (self.checkWallX(node.x, restnode.x, node.y)):
                        distance = abs(node.y - restnode.y)
                        if (node.x > restnode.x): d1, d2 = left, right
                        else: d1,d2 = right, left
                        node.connect(restnode, distance, d1)
                        restnode.connect(node, distance, d2)
                        neighbours += 1
                if (neighbours >= 4):
                    break

    # Function to check if the two nodes you are checking are on a valid path in x and y direction
    def checkWallX(self, a, b, y):
        start = a if a < b else b
        end = a if a > b else b
        for x in range(start, end):
            if (self.image.getpixel((x,y)) == black):
                return False
        return True

    def checkWallY(self, a, b, x):
        start = a if a < b else b
        end = a if a > b else b
        for y in range(start, end):
            if (self.image.getpixel((x,y)) == black):
                return False
        return True
# endregion

# region => Visualize Nodes
    def showNodes(self):
        for i in self.nodes:
            if (i.isStart):
                self.imageNodes.putpixel((i.x, i.y), green)
            elif(i.isEnd):
                self.imageNodes.putpixel((i.x, i.y), blue)
            else:
                self.imageNodes.putpixel((i.x, i.y), red)
    
    def showPath(self):
        pass
# endregion