import argparse
from PIL import Image

def main(filename: str):
    directory =  'C:/Users/Tijmen/Desktop/Stack/Projects/Python/Maze-Solver/Images/'
    #directory = 'D:/Stack Sync Folder/Projects/Python/Maze-Solver/Images/'
    filename = '10.png'
    path = directory + filename
    image = Image.open(path)
    maze = maze(image)

if __name__ == '__main__':
    main()