from src.board import Board

class NaiveSolver:
    def __init__(self, board):
        self.board = board
        self.attempts = 0

    def solve(self):
        self.attempts += 1
        empty = self.board.find_empty()
        if not empty:
            return True  # Solved
        row, col = empty

        for num in range(1, 10):
            if self.board.is_valid(row, col, num):
                self.board.set_cell(row, col, num)

                if self.solve():
                    return True

                self.board.set_cell(row, col, 0)  # Backtrack

        return False  # Trigger backtracking

    @property
    def attempt_count(self):
        return self.attempts
