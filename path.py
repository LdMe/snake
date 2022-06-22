from snake import Snake
from direction import Direction

class Path:

    def __init__(self,snake_body,board,depth):
        self.snake = Snake(snake_body,board)
        self.depth = depth

    def run(self,snake,depth):
        if(depth == 0):
            return []

        options = []
        for direction in Direction:
            if(snake.can_move(direction)):
                new_snake = snake.copy()
                new_snake.move(direction)
                result = self.run(new_snake,depth-1)
                if(len(result) == 0):
                    options.append(direction.name)
                else:
                    for r in result:
                        options.append(direction.name + r)
        return options
    
    def get_num_paths(self,snake,depth):
        return len(self.run(snake,depth))