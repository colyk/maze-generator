# Maze-generator
Simple gui and text maze generator

### Sample of work...

  >  ![alt text](https://image.ibb.co/nqeQaG/maze.png)
  
### Sample of gui maze generation  

```
from maze_generator import Maze

game = Maze(35, 60) # 35 - width of gui window, 60 - height of window
game.gui_maze(10)   # 10 pixel width
```
    
### Sample of text maze generation  

```
from maze_generator import Maze

game = Maze(35, 60) # 35 - width of gui window, 60 - height of window
game.text_maze()
```
