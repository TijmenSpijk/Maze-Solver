import argparse
import solve
from maze import Maze
from PIL import Image

def main():
    directory =  'C:/Users/Tijmen/Desktop/Stack/Projects/Python/Maze-Solver/Images/'
    # directory = 'D:/Stack Sync Folder/Projects/Python/Maze-Solver/Images/'
    filename = '100.png'
    path = directory + filename
    image = Image.open(path)
    # image.show()
    maze = Maze(image)
    maze.showNodes()
    # solve(maze)

if __name__ == '__main__':
    main()