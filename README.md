# Snake
## Problem

### Calculate the amount of valid paths for a snake inside a board for a given depth

Knowing the size of the board, the positions of the body of the snake and the depth (number of steps for a given path), we want to know how many paths we can get without going outside the board or intersecting with its own body.

#### Example

For board = [4, 3], snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]], and depth = 3, the output
should be “numberOfAvailableDifferentPaths(board, snake, depth) = 7”.

Here are all of the valid paths with a length of 3 that the snake can make:
* UUL
* LUR
* LUL
* ULL
* ULD
* LUU
* ULU

## Solution

My python based solution consists of three objects:
* An enumeration called "Direction" that translates a letter (U,D,L,R) to an array.
* A "Snake" class to handle movements.
* A "Path" class to get all the possible paths for certain initial values.

To get the number of possible paths, you should run the following lines:

```
from path import Path

path = Path(snake_body,board,depth)
possible_path_number = path.get_num_paths(path.snake,path.depth)

```
Where snake_body is a list of bidimensional positions, board is a bidimensional list and depth is an integer.

Example:

```
from path import Path

snake_body = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
board = [4,3]
depth = 3

path = Path(snake_body,board,depth)
possible_path_number = path.get_num_paths(path.snake,path.depth)
print(possible_path_number)

```
output:

```
7
```



We can also get a list of all the possible paths, with each letter of the path indicating the direction of each step:

```
from path import Path

path = Path(snake_body,board,depth)
possible_paths = path.run(path.snake,path.depth)

```

Example:

```
from path import Path

snake_body = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
board = [4,3]
depth = 3

path = Path(snake_body,board,depth)
possible_paths = path.run(path.snake,path.depth)
print(possible_paths)

```
Output:
```
['LUL', 'LUR', 'LUU', 'ULL', 'ULU', 'ULD', 'UUL']
```
