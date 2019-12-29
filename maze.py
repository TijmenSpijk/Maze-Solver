from PIL  import Image
from node import Node
#some global colors
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red   = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue  = (0, 0, 255, 255)

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
        self.createNodes()

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

# region => Visualize Nodes
    def showNodes(self):
        copy = self.image.copy()
        for i in self.nodes:
            if (i.isStart):
                copy.putpixel((i.x, i.y), green)
            elif(i.isEnd):
                copy.putpixel((i.x, i.y), blue)
            else:
                copy.putpixel((i.x, i.y), red)
        copy.show()
    
    def showPath(self):
        pass
# endregion