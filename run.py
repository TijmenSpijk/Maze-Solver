import argparse
import solve
from tkinter import filedialog
from tkinter import *
from maze import Maze
from PIL import Image

def main():
    root = Tk()
    root.withdraw()
    directory =  'C:/Users/Tijmen/Desktop/Stack/Projects/Python/Maze-Solver/Images/'
    # directory = 'D:/Stack Sync Folder/Projects/Python/Maze-Solver/Images/'
    filename = '10.png'
    path = openFile(directory)
    image = Image.open(path)
    maze = Maze(image)
    maze.showNodes()
    saveFile(directory, maze.imageNodes)
    # solve(maze)

def openFile(directory):    
    filename = filedialog.askopenfilename(initialdir = directory, title = "Select Maze", filetypes = (("png files","*.png"),("all files","*.*")))
    return filename

def saveFile(directory, image):
    filename = filedialog.asksaveasfilename(initialdir = directory, defaultextension='.png',filetypes=(('PNG files', '*.png'),('All files', '*.*')))
    if filename != None:
        image.save(filename)
    return

if __name__ == '__main__':
    main()