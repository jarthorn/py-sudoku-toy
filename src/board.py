class Board:
    def __init__(self, board):
        import copy
        self.board = copy.deepcopy(board)

    def get_cell(self, row, col):
        return self.board[row][col]

    def set_cell(self, row, col, value):
        self.board[row][col] = value

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r, c)
        return None

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

    def is_valid(self, row, col, num):
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

    def __str__(self):
        lines = []
        sep = "+-------+-------+-------+"
        for i, row in enumerate(self.board):
            if i % 3 == 0:
                lines.append(sep)
            line = "|"
            for j, num in enumerate(row):
                line += " " + (str(num) if num != 0 else ".")
                if j % 3 == 2:
                    line += " |"
            lines.append(line)
        lines.append(sep)
        return "\n".join(lines)
