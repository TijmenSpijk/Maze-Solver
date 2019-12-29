from node import Node
#some global colors
white = (255, 255, 255, 0)
black = (0, 0, 0, 0)
red   = (255, 0, 0, 0)
green = (0, 255, 0, 0)
blue  = (0, 0, 255, 0)

# {
#   The Maze Class:
#   The class to convert the image into a maze
#   The maze is defined by a set of connected nodes
# }
class Maze:
    def __init__(self, image: Image):
        self.image = image
        self.width = image.width
        self.height = image.height
        self.nodes = []

    # Function to conver the image into a set of connected nodes
    def createNodes(self):
        xstart, ystart = self.findStart(), 1
        start = Node(xstart, ystart)
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
                    elif (self.isDeadEnd(i, j)):
                        node = Node(i, j)
                        self.nodes.append(node)
                    # Dead End

    # Function to check if a certain pixel is a corner of the maze
    def isCorner(self, x, y):
        pass
    # Function to chek if a certain pixel is a t-split in the maze
    def isTSplit(self, x, y):
        pass
    # Funtion to check if a certain pixel is a dead-end in the maze
    def isDeadEnd(self, x, y):
        pass

    # Funtion to find the start node of the maze
    def findStart(self):
        for i in range(self.width):
            if (self.image.getpixel((i, 1)) == (255, 255, 255, 0)):
                return i
        return None

    # Function to find the end node of the maze
    def findEnd(self):
        for i in range(self.width):
            if (self.image.getpixel((i, self.height - 1)) == (255, 255, 255, 0)):
                return i
        return None
