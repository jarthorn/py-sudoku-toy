
import unittest
from src.board import Board
from src.candidate_solver import CandidateSolver
from src.naive_solver import NaiveSolver

class TestSolverSuite(unittest.TestCase):
    def setUp(self):
        self.solver_classes = [NaiveSolver, CandidateSolver]
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
        self.medium_puzzle = [
            [7, 0, 0, 0, 0, 0, 6, 0, 0],
            [0, 0, 6, 7, 5, 0, 4, 0, 0],
            [5, 0, 0, 6, 1, 0, 0, 8, 0],
            [8, 0, 1, 0, 0, 0, 0, 9, 0],
            [0, 0, 0, 2, 0, 3, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 2, 0, 4],
            [0, 5, 0, 0, 4, 6, 0, 0, 9],
            [0, 0, 4, 0, 3, 5, 1, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 3]
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
        self.hard_puzzle = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ]

    def test_solve_easy_puzzle(self):
        for SolverClass in self.solver_classes:
            board = Board(self.easy_puzzle)
            solver = SolverClass(board)
            solver.solve()
            if not board.is_solved():
                print(board)
            self.assertTrue(board.is_solved(), f"{SolverClass.__name__} failed to solve easy puzzle")

    def test_solve_medium_puzzle(self):
        for SolverClass in self.solver_classes:
            board = Board(self.medium_puzzle)
            solver = SolverClass(board)
            solver.solve()
            if not board.is_solved():
                print(f"{SolverClass.__name__} failed to solve medium puzzle:")
            print(board)
            self.assertTrue(board.is_solved(), f"{SolverClass.__name__} failed to solve medium puzzle")

    def test_solve_hard_puzzle(self):
        for SolverClass in self.solver_classes:
            board = Board(self.hard_puzzle)
            solver = SolverClass(board)
            solver.solve()
            # print(f"{SolverClass.__name__} attempts: {solver.attempt_count}")
            if not board.is_solved():
                print(f"{SolverClass.__name__} failed to solve hard puzzle:")
                print(board)
            self.assertTrue(board.is_solved(), f"{SolverClass.__name__} failed to solve hard puzzle")

    def test_unsolvable_puzzle(self):
        for SolverClass in self.solver_classes:
            board = Board(self.unsolvable_puzzle)
            solver = SolverClass(board)
            solver.solve()
            self.assertFalse(board.is_solved(), f"{SolverClass.__name__} incorrectly solved unsolvable puzzle")

if __name__ == '__main__':
    unittest.main()
