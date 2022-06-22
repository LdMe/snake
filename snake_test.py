from snake import Snake
from direction import Direction
import unittest

class SnakeTest(unittest.TestCase):
    def setUp(self):
        self.snake = Snake([[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]],[4, 3])

    def test_is_out_of_range(self):
        self.assertTrue(self.snake.is_out_of_range(4,4))
        self.assertTrue(self.snake.is_out_of_range(-1,4))
        self.assertFalse(self.snake.is_out_of_range(1,4))

    def test_is_out_of_bounds(self):
        self.assertTrue(self.snake.is_out_of_bounds([4,0]))
        self.assertTrue(self.snake.is_out_of_bounds([4,-1]))
        self.assertFalse(self.snake.is_out_of_bounds([3,0]))

        self.assertTrue(self.snake.is_out_of_bounds([1,3]))
        self.assertTrue(self.snake.is_out_of_bounds([-1,1]))
        self.assertFalse(self.snake.is_out_of_bounds([3,2]))

        self.assertTrue(self.snake.is_out_of_bounds([4,3]))

    def test_intersects(self):
        for body_part in self.snake.body[:-1]:
            self.assertTrue(self.snake.intersects(body_part))
        self.assertFalse(self.snake.intersects([2,1]))

    def test_move_body(self):
        self.snake.move_body([2,1])
        self.assertEqual(self.snake.body,[[2,1],[2,2], [3,2], [3,1], [3,0], [2,0], [1,0] ])

        self.snake.move_body([1,1])
        self.assertEqual(self.snake.body,[[1,1],[2,1],[2,2], [3,2], [3,1], [3,0], [2,0] ])

    def test_add_direction(self):
        self.assertEqual(self.snake.add_direction([0,0],Direction.U),[-1,0])
        self.assertEqual(self.snake.add_direction([0,0],Direction.D),[1,0])
        self.assertEqual(self.snake.add_direction([0,0],Direction.L),[0,-1])
        self.assertEqual(self.snake.add_direction([0,0],Direction.R),[0,1])

    def test_can_move(self):
        self.setUp()
        self.assertTrue(self.snake.can_move(Direction.U))
        self.assertEqual(self.snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])

        self.setUp()
        self.assertFalse(self.snake.can_move(Direction.D))   
        self.assertEqual(self.snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])

        self.setUp()
        self.assertTrue(self.snake.can_move(Direction.L))  
        self.assertEqual(self.snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])

        self.setUp()
        self.assertFalse(self.snake.can_move(Direction.R))  
        self.assertEqual(self.snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])

        self.snake = Snake([[1, 2], [2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0]],[4, 3])
        self.assertFalse(self.snake.can_move(Direction.R)) 
        self.assertEqual(self.snake.body,[[1, 2], [2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0]])
 

    def test_move(self):
        self.setUp()
        self.assertEqual(self.snake.move(Direction.U),1)
        self.assertEqual(self.snake.body,[[1,2],[2,2], [3,2], [3,1], [3,0], [2,0], [1,0]])

        self.setUp()
        self.assertEqual(self.snake.move(Direction.D),-1)   
        self.assertEqual(self.snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])

        self.setUp()
        self.assertEqual(self.snake.move(Direction.L),1)  
        self.assertEqual(self.snake.body,[[2,1],[2,2], [3,2], [3,1], [3,0], [2,0], [1,0]])

        self.setUp()
        self.assertEqual(self.snake.move(Direction.R),-1)  
        self.assertEqual(self.snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])

    def test_copy(self):
        self.setUp()
        new_snake = self.snake.copy()
        self.snake.move(Direction.U)
        self.assertEqual(new_snake.body,[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])



if __name__ == "__main__":
    unittest.main()