class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Solved
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  # Backtrack

        return False  # Trigger backtracking

    def is_solved(self):
        # Check rows
        for row in self.board:
            if sorted(row) != list(range(1, 10)):
                return False

        # Check columns
        for col in range(9):
            column = [self.board[row][col] for row in range(9)]
            if sorted(column) != list(range(1, 10)):
                return False

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(self.board[r][c])
                if sorted(box) != list(range(1, 10)):
                    return False

        return True

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r, c)  # Row, Col
        return None

    def is_valid(self, num, row, col):
        # Check row
        if num in self.board[row]:
            return False

        # Check column
        if num in (self.board[r][col] for r in range(9)):
            return False

        # Check 3x3 box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if self.board[r][c] == num:
                    return False

        return True
