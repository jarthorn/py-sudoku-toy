class CandidateSolver:
    def __init__(self, board):
        self.board = board
        # Candidates: 9x9 grid of strings, each string contains possible digits for that cell
        self.candidates = [["123456789" if self.board.get_cell(r, c) == 0 else str(self.board.get_cell(r, c))
                            for c in range(9)] for r in range(9)]
        self.attempts = 0

    def solve(self):
        changed = True
        while changed:
            self.attempts += 1
            if self.board.is_solved():
                break
            changed = False
            for heuristic in self.heuristics():
                if heuristic():
                    changed = True
        return self.board.is_solved()

    def heuristics(self):
        # List of heuristic methods to apply
        return [self.eliminate_by_row, self.eliminate_by_col, self.eliminate_by_box]

    def eliminate_by_row(self):
        changed = False
        for r in range(9):
            # Collect solved values in the row
            solved = [str(x) for x in self.board.get_row(r) if x != 0]
            for c in range(9):
                if len(self.candidates[r][c]) > 1:
                    before = self.candidates[r][c]
                    # Remove solved values from candidate string
                    for val in solved:
                        self.candidates[r][c] = self.candidates[r][c].replace(val, "")
                    if self.candidates[r][c] != before:
                        changed = True
                        # If only one candidate remains, update the board
                        if len(self.candidates[r][c]) == 1:
                            self.board.set_cell(r, c, int(self.candidates[r][c]))
        return changed

    def eliminate_by_col(self):
        changed = False
        for c in range(9):
            # Collect solved values in the column using board.get_col, matching row style
            solved = set(str(val) for val in self.board.get_col(c) if val != 0)
            for r in range(9):
                if len(self.candidates[r][c]) > 1:
                    before = self.candidates[r][c]
                    # Remove solved values from candidate string
                    for val in solved:
                        self.candidates[r][c] = self.candidates[r][c].replace(val, "")
                    if self.candidates[r][c] != before:
                        changed = True
                        # If only one candidate remains, update the board
                        if len(self.candidates[r][c]) == 1:
                            self.board.set_cell(r, c, int(self.candidates[r][c]))
        return changed

    def eliminate_by_box(self):
        changed = False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                # Collect solved values in the box
                solved = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = self.board.get_cell(r, c)
                        if val != 0:
                            solved.add(str(val))
                # Remove solved values from candidates in the box
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if len(self.candidates[r][c]) > 1:
                            before = self.candidates[r][c]
                            for val in solved:
                                self.candidates[r][c] = self.candidates[r][c].replace(val, "")
                            if self.candidates[r][c] != before:
                                changed = True
                                if len(self.candidates[r][c]) == 1:
                                    self.board.set_cell(r, c, int(self.candidates[r][c]))
        return changed
    @property
    def attempt_count(self):
        return self.attempts
