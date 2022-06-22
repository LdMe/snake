
from direction import Direction
class Snake:

    def __init__(self,body,board):
        self.body = body
        # board[0] is the number of rows (y) and board[1] is the number of columns[x]
        self.max_x = board[1]
        self.max_y = board[0]
        self.length = len(self.body)

    def move(self,direction):
        new_head = self.add_direction(self.body[0],direction)
        if(self.is_out_of_bounds(new_head)):
            return -1
        if(self.intersects(new_head)):
            return -1
        self.move_body(new_head)
        return 1

    def add_direction(self,position,direction):
        direction_values = direction.value
        new_position = [position[0] + direction_values[0],position[1] +  direction_values[1] ]
        return new_position
    def move_body(self,new_position):
        for i in range(1, self.length ):
            actual_position = -i
            next_position = -(i+1)
            self.body[actual_position] = self.body[next_position]
        self.body[0] = new_position
    def is_tail(self,position):
        return position == self.body[-1]

    def intersects(self,position):
        for body_part in self.body[:-1]:
            if(position == body_part):
                return True
        return False

    def is_out_of_bounds(self, position):
        x = position[1]
        y = position[0]
        if(self.is_out_of_range(x,self.max_x) or self.is_out_of_range(y,self.max_y)):
            return True
        return False
    def is_out_of_range(self,num,max):
        if(num >= max or num < 0):
            return True
        return False

    def __str__(self):
        return str(self.body)

        