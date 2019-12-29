import argparse
from PIL import Image

def main(filename: str):
    directory =  'C:/Users/Tijmen/Desktop/Stack/Projects/Python/MazeSolver/Images/'
    #directory = 'D:/Stack Sync Folder/Projects/Python/MazeSolver/Images/'
    path = directory + filename
    image = Image.open(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Give the path to the maze image')
    args = parser.parse_args()
    main(str(args.path))