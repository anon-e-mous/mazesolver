import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        total = 0
        for col in range(num_cols):
            for row in range(num_rows):
                if m1._cells[col][row].visited == False:
                    total += 1
        self.assertEqual(total,
            num_cols * num_rows,
        )










if __name__ == "__main__":
    unittest.main()