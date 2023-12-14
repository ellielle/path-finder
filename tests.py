import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 16
        m2_num_cols = 20
        m2_num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2 = Maze(20, 20, m2_num_rows, m2_num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        self.assertEqual(len(m2._cells), m2_num_cols)
        self.assertEqual(len(m2._cells[0]), m2_num_rows)

    def test_maze_creation_fail(self):
        with self.assertRaises(ValueError) as context:
            Maze(0, 0, 0, 0, 10, 10)

        self.assertTrue("Rows and Columns can't be 0" in str(context.exception))

    def test_entrance_and_exit_creation(self):
        maze = Maze(20, 20, 10, 12, 20, 20)
        m2 = Maze(0, 0, 1, 1, 20, 20)
        maze_entrance = maze._cells[0][0]
        maze_exit = maze._cells[-1][-1]
        m2_entrance = maze._cells[0][0]
        m2_exit = m2._cells[-1][-1]
        self.assertFalse(maze_entrance.has_top_wall)
        self.assertFalse(maze_exit.has_bottom_wall)
        self.assertFalse(m2_entrance.has_top_wall)
        self.assertFalse(m2_exit.has_top_wall)

    def test_break_walls(self):
        not_broken = []
        maze = Maze(20, 20, 10, 12, 20, 20)
        cells = maze.get_cells()
        for columns in cells:
            for cell in columns:
                if (
                    not cell.has_left_wall
                    and cell.has_right_wall
                    and cell.has_top_wall
                    and cell.has_bottom_wall
                ):
                    not_broken.append(cell)

        raise Exception(len(not_broken))
        self.assertTrue(len(not_broken) == 0)


#    def test_visited_reset(self):
#        cells_reset = False
#        maze = Maze(20, 20, 20, 20, 20, 20, None, "testing")
#        cells = maze.get_cells()
#        for columns in cells:
#            for cell in columns:
#                if not cell.visited:
#                    cells_reset = False
#                    break
#                else:
#                    cells_reset = True
#
#        self.assertTrue(cells_reset)


if __name__ == "__main__":
    unittest.main()
