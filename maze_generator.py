import sys
import random
from tkinter import *

class Maze(object):
    def __init__(self, width=35, height=21, recursion_limit=2000):
        self.check_size(width, height)
        self.maze = dict()
        try:
            sys.setrecursionlimit(recursion_limit)
        except Exception as e:
            print(e)
 
    def check_size(self, width, height):
        """width and heighr must be odd"""
        if width%2 == 0:
            self.width = width + 1
        else:
            self.width = width

        if height%2 == 0:
            self.height = height + 1
        else:
            self.height = height

    def init_maze(self):
        for x in range(0, self.width):
            self.maze[x] = dict()
            for y in range(0, self.height):
                self.maze[x][y] = 1

    def carve_maze(self, x, y):
        dir = random.randint(0, 3)
        count = 0
        while count < 4:
            dx = 0
            dy = 0
            if dir == 0:
               dx = 1
            elif dir == 1:
               dy = 1
            elif dir == 2:
               dx = -1
            else:
               dy = -1
            x1 = x + dx
            y1 = y + dy
            x2 = x1 + dx
            y2 = y1 + dy
            if x2 > 0 and x2 < self.width and y2 > 0 and y2 < self.height:
               if self.maze[x1][y1] == 1 and self.maze[x2][y2] == 1:
                  self.maze[x1][y1] = 0
                  self.maze[x2][y2] = 0
                  self.carve_maze(x2, y2)
            count = count + 1
            dir = (dir + 1) % 4

    def generate_maze(self):
        random.seed()
        self.maze[1][1] = 0
        try:
            self.carve_maze(1, 1)
        except Exception:
            print('Size of maze is too big!')
            sys.exit(1)
        self.maze[1][0] = 0
        self.maze[self.width - 2][self.height - 1] = 0

    def gui_maze(self, wall_size=10):
        tk = Tk()
        wall = wall_size
        tk_width = self.width * wall + 1
        tk_height = self.height * wall + 1
        tk.title(u'Maze generator')
        tk.geometry('{}x{}+100+100'.format(tk_width, tk_height)) 
        tk.resizable(False, False)
        c = Canvas(tk, width=tk_width, height=tk_height)
        c.pack()
        def rebuild_maze(event):
            tk.destroy()
            self.gui_maze()
        tk.bind("<Button-1>", rebuild_maze)

        self.init_maze()
        self.generate_maze()
        x0, y0, x1, y1 = 0, 0, wall, wall

        for y in range(self.height-1, -1, -1):
            for x in range(self.width-1, -1, -1):
                if self.maze[x][y] == 0:
                    c.create_rectangle(x0, y0, x1, y1, fill = 'white', width = 0)
                else:
                    c.create_rectangle(x0, y0, x1, y1, fill = 'black', width = 0)
                x0 += wall
                x1 += wall
            x0 = 0
            y0 += wall
            x1 = wall
            y1 += wall
        c.create_rectangle(wall+1, wall+1, 2*wall-1, 2*wall-1, fill = '#0ED100', width = 0)
        c.create_rectangle(tk_width-2*wall, tk_height-2*wall, tk_width-wall-1, tk_height-wall-1, fill = '#D6000A', width = 0)
        tk.mainloop()
    
    def text_maze(self):
        self.init_maze()
        self.generate_maze()
        try:
            self.maze[1][0] = ' @ '
            self.maze[self.height-2][self.width-1] = ' * '
        except:
            pass
        for y in range(self.height-1, -1, -1):
            for x in range(self.width-1, -1, -1):
                if self.maze[x][y] == 0:
                    sys.stdout.write("   ")
                elif self.maze[x][y] == 1:
                    sys.stdout.write("[!]")
                else:
                    sys.stdout.write(self.maze[x][y])
            sys.stdout.write("\n")

if __name__ == '__main__':
    game = Maze(35,60)
    game.gui_maze(10)
    game.text_maze()
