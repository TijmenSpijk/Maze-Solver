import argparse
import solve
from tkinter import filedialog, messagebox
from tkinter import *
from maze import Maze
from PIL import Image

dfs = 1
bfs = 2
dstr = 3
astar = 4

def main():
    root = Tk()
    root.withdraw()
    directory =  '../Maze-Solver/Images'
    # if(messagebox.askyesno(title='Generate?', message='Do you have a maze to solve? (NO => I will generate one)')):
    #     filepath = openFile(directory)
    # else :
    #     generated_maze = generateMaze()
    filepath = openFile(directory)
    image = Image.open(filepath)
    maze = Maze(image)
    maze.showNodes()
    if(messagebox.askyesno(title='Save Node Image?', message='Do you want to save the nodes')):
        saveFile(directory, maze.imageNodes)
    solution = solve.solve(maze, dfs)
    maze.showPath(solution)
    if(messagebox.askyesno(title='Save?', message='Do you want to save the solution')):
        saveFile(directory, maze.imagePath)

def openFile(directory):    
    filename = filedialog.askopenfilename(initialdir = directory, title = "Select Maze", filetypes = (("png files","*.png"),("all files","*.*")))
    return filename

def saveFile(directory, image):
    filename = filedialog.asksaveasfilename(initialdir = directory, defaultextension='.png',filetypes=(('PNG files', '*.png'),('All files', '*.*')))
    if filename != None:
        image.save(filename)
    return

def generateMaze():
    pass

if __name__ == '__main__':
    main()