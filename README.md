# Maze generator
GUI and console maze generator.

### How it works
GUI version
<img src="https://i.ibb.co/F6MTcdq/photo-2023-04-30-23-48-15.jpg" alt="GUI example" height="400">

Console version
<img src="https://i.ibb.co/7yFb4PM/photo-2023-04-30-23-48-17.jpg" alt="Console version" height="400">
  
### How to run
GUI version

```python
maze = Maze(width=35, height=60)
maze.gui_maze(wall_size=10)
```
    
Console version

```python
maze = Maze(width=15, height=30)
maze.text_maze()
```
