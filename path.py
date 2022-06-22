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
                new_snake = self.copy_snake_and_move(snake,direction)
                result = self.run(new_snake,depth-1)
                options = self.append_paths(direction,options,result)
        return options
    
    def append_paths(self,direction,paths,result):
        if(len(result) == 0):
            paths.append(direction.name)
        else:
            for r in result:
                paths.append(direction.name + r)
        return paths

    def copy_snake_and_move(self,snake,direction):
        new_snake = snake.copy()
        new_snake.move(direction)
        return new_snake
        
    def get_num_paths(self,snake,depth):
        return len(self.run(snake,depth))