import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        unsolved_input = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.board = Board(unsolved_input)

    def test_get_set_cell(self):
        self.assertEqual(self.board.get_cell(2, 1), 9)
        self.assertEqual(self.board.get_cell(0, 2), 0)
        self.board.set_cell(0, 2, 4)
        self.assertEqual(self.board.get_cell(0, 2), 4)

    def test_find_empty(self):
        empty = self.board.find_empty()
        self.assertIsInstance(empty, tuple)
        self.assertEqual(empty, (0, 2))
        self.board.set_cell(0, 2, 4)
        empty = self.board.find_empty()
        self.assertEqual(empty, (0, 3))

    def test_is_valid(self):
        # 4 is valid at (0, 2)
        self.assertTrue(self.board.is_valid(0, 2, 4))
        # 5 is not valid at (0, 2) because 5 is already in the row
        self.assertFalse(self.board.is_valid(0, 2, 5))
        # 8 is not valid at (0, 2) because 8 is already in the column
        self.assertFalse(self.board.is_valid(0, 2, 8))
        # 9 is not valid at (0, 2) because 9 is already in the 3x3 box
        self.assertFalse(self.board.is_valid(0, 2, 9))

    def test_is_solved_false(self):
        self.assertFalse(self.board.is_solved())

if __name__ == '__main__':
    unittest.main()