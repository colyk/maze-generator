# Maze generator
GUI and console maze generator.

### How it works
GUI version
  >  ![GUI example](https://i.ibb.co/F6MTcdq/photo-2023-04-30-23-48-15.jpg)
Console version
  >  ![console example](https://i.ibb.co/7yFb4PM/photo-2023-04-30-23-48-17.jpg)
  
### How to run
GUI version

```python
from maze_generator import Maze

maze = Maze(width=35, height=60)
maze.gui_maze(wall_size=10)
```
    
Console version

```python
from maze_generator import Maze

maze = Maze(width=35, height=60)
maze.text_maze()
```
