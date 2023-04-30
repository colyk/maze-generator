import sys
import random
from tkinter import *


class Maze:
    def __init__(self, width: int = 35, height: int = 21, recursion_limit: int = 1000):
        # Width and height must be odd numbers.
        self.width = width + 1 if width % 2 == 0 else width
        self.height = height + 1 if height % 2 == 0 else height
        self.maze = dict()

        sys.setrecursionlimit(recursion_limit)

    def _generate_maze(self):
        self._init_maze()
        random.seed()
        self.maze[1][1] = 0
        try:
            self._carve_maze(1, 1)
        except RecursionError:
            print("Set bigger Maze(recursion_limit=1000) parameter")
            raise
        self.maze[1][0] = 0
        self.maze[self.width - 2][self.height - 1] = 0

    def _init_maze(self):
        for i in range(0, self.width):
            self.maze[i] = dict()
            for y in range(0, self.height):
                self.maze[i][y] = 1

    def _carve_maze(self, x, y):
        direction = random.randint(0, 3)
        step_count = 0
        while step_count < 4:
            dx = 0
            dy = 0
            if direction == 0:
                dx = 1
            elif direction == 1:
                dy = 1
            elif direction == 2:
                dx = -1
            else:
                dy = -1

            x1 = x + dx
            y1 = y + dy
            x2 = x1 + dx
            y2 = y1 + dy
            if 0 < x2 < self.width and 0 < y2 < self.height:
                if self.maze[x1][y1] == 1 and self.maze[x2][y2] == 1:
                    self.maze[x1][y1] = 0
                    self.maze[x2][y2] = 0
                    self._carve_maze(x2, y2)
            step_count += 1
            direction = (direction + 1) % 4

    def gui_maze(self, wall_size: int = 10):
        tk = Tk()
        tk.title("Maze generator")
        tk_width = self.width * wall_size + 1
        tk_height = self.height * wall_size + 1
        tk.geometry(f"{tk_width}x{tk_height}+100+100")
        tk.resizable(False, False)
        canvas = Canvas(tk, width=tk_width, height=tk_height)
        canvas.pack()

        def rebuild_maze(_):
            tk.destroy()
            self.gui_maze()

        tk.bind("<Button-1>", rebuild_maze)

        self._generate_maze()
        x0, y0, x1, y1 = 0, 0, wall_size, wall_size
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width - 1, -1, -1):
                fill = "white" if self.maze[x][y] == 0 else "black"
                canvas.create_rectangle(x0, y0, x1, y1, fill=fill, width=0)
                x0 += wall_size
                x1 += wall_size
            x0 = 0
            x1 = wall_size
            y0 += wall_size
            y1 += wall_size
        canvas.create_rectangle(
            wall_size + 1,
            wall_size + 1,
            2 * wall_size - 1,
            2 * wall_size - 1,
            fill="#0ED100",
            width=0,
        )
        canvas.create_rectangle(
            tk_width - 2 * wall_size,
            tk_height - 2 * wall_size,
            tk_width - wall_size - 1,
            tk_height - wall_size - 1,
            fill="#D6000A",
            width=0,
        )
        tk.mainloop()

    def text_maze(
        self, start_char: str = "@", end_char: str = "*", wall_str: str = "[!]"
    ) -> None:
        self._generate_maze()
        self.maze[1][0] = f" {start_char} "
        self.maze[self.width - 2][self.height - 1] = f" {end_char} "

        for y in range(self.height - 1, -1, -1):
            for x in range(self.width - 1, -1, -1):
                if self.maze[x][y] == 0:
                    sys.stdout.write("   ")
                elif self.maze[x][y] == 1:
                    sys.stdout.write(wall_str)
                else:
                    sys.stdout.write(self.maze[x][y])
            sys.stdout.write("\n")


if __name__ == "__main__":
    maze = Maze(width=30, height=50)
    maze.gui_maze(wall_size=10)
    maze.text_maze()
