
import unittest
from src.board import Board
from src.solver import NaiveSolver

class TestSolverSuite(unittest.TestCase):
    def setUp(self):
        self.solver_classes = [NaiveSolver]
        self.easy_puzzle = [
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
        self.unsolvable_puzzle = [
            [5, 5, 0, 0, 7, 0, 0, 0, 0],  # Invalid: two 5's in the first row
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    def test_solve_easy_puzzle(self):
        for SolverClass in self.solver_classes:
            board = Board(self.easy_puzzle)
            solver = SolverClass(board)
            solver.solve()
            self.assertTrue(solver.is_solved(), f"{SolverClass.__name__} failed to solve easy puzzle")

    def test_unsolvable_puzzle(self):
        for SolverClass in self.solver_classes:
            board = Board(self.unsolvable_puzzle)
            solver = SolverClass(board)
            solver.solve()
            self.assertFalse(solver.is_solved(), f"{SolverClass.__name__} incorrectly solved unsolvable puzzle")

if __name__ == '__main__':
    unittest.main()
