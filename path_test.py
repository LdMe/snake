from path import Path
from direction import Direction
import unittest

class PathTest(unittest.TestCase):
    def setUp(self):
        self.path = Path([[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]],[4, 3],3)


    def test_append_paths(self):
        self.assertEqual(self.path.append_paths(Direction.L,["LU"],[]),["LU","L"])
        self.assertEqual(self.path.append_paths(Direction.L,["LU"],["D","U"]),["LU","LD","LU"])

    def test_run(self):
        self.assertEqual(self.path.run(self.path.snake,self.path.depth),['LUL', 'LUR', 'LUU', 'ULL', 'ULU', 'ULD', 'UUL'])
        
    def test_get_num_paths(self):
        self.path = Path([[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]],[4, 3],3)
        self.assertEqual(self.path.get_num_paths(self.path.snake,self.path.depth),7)

        self.path = Path([[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]],[2, 3],10)
        self.assertEqual(self.path.get_num_paths(self.path.snake,self.path.depth),1)

        self.path = Path([[5,5], [5,4], [4,4], [4,5]],[10, 10],4)
        self.assertEqual(self.path.get_num_paths(self.path.snake,self.path.depth),81)

    

if __name__ == "__main__":
    unittest.main()