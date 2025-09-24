class CandidateSolver:

    def __str__(self):
        lines = []
        for r in range(9):
            row = []
            for c in range(9):
                cell = self.candidates[r][c]
                row.append(cell.center(9))
            lines.append(" | ".join(row))
            if r % 3 == 2 and r != 8:
                lines.append("-" * (9 * 10 - 1))
        return "\n".join(lines)

    def __init__(self, board):
        self.board = board
        # Candidates: 9x9 grid of strings, each string contains possible digits for that cell
        self.candidates = [["123456789" if self.board.get_cell(r, c) == 0 else str(self.board.get_cell(r, c))
                            for c in range(9)] for r in range(9)]
        self.attempts = 0

    @property
    def attempt_count(self):
        return self.attempts

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
        return [
            self.eliminate_by_row,
            self.eliminate_by_col,
            self.eliminate_by_box,
            self.only_candidate_by_row,
            self.only_candidate_by_col,
            self.only_candidate_by_box
        ]

    def only_candidate_by_row(self):
        changed = False
        for r in range(9):
            for digit in "123456789":
                candidate_cells = [(r,c) for c in range(9) if digit in self.candidates[r][c]]
                if self._update_only_candidate(candidate_cells, digit):
                    changed = True
        return changed

    def _update_only_candidate(self, candidate_cells, digit):
        if len(candidate_cells) == 1 and self.board.get_cell(*candidate_cells[0]) == 0:
            (r,c) = candidate_cells[0]
            self.candidates[r][c] = digit
            self.board.set_cell(r, c, int(digit))
            return True
        return False

    def only_candidate_by_col(self):
        changed = False
        for c in range(9):
            for digit in "123456789":
                candidate_cells = [(r, c) for r in range(9) if digit in self.candidates[r][c]]
                if self._update_only_candidate(candidate_cells, digit):
                    changed = True
        return changed

    def only_candidate_by_box(self):
        changed = False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for digit in "123456789":
                    candidate_cells = [
                        (r, c)
                        for r in range(box_row, box_row + 3)
                        for c in range(box_col, box_col + 3)
                        if digit in self.candidates[r][c]
                    ]
                    if (self._update_only_candidate(candidate_cells, digit)):
                        changed = True
        return changed

    def eliminate_by_row(self):
        changed = False
        for r in range(9):
            solved = [str(value) for value in self.board.get_row(r) if value != 0]
            cells = [(r, c) for c in range(9)]
            if self._eliminate_candidates(cells, solved):
                changed = True
        return changed

    def eliminate_by_col(self):
        changed = False
        for c in range(9):
            solved = [str(value) for value in self.board.get_col(c) if value != 0]
            cells = [(r, c) for r in range(9)]
            if self._eliminate_candidates(cells, solved):
                changed = True
        return changed

    def eliminate_by_box(self):
        changed = False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                solved = [str(self.board.get_cell(r, c)) for r in range(box_row, box_row + 3)
                          for c in range(box_col, box_col + 3) if self.board.get_cell(r, c) != 0]
                cells = [(r, c) for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                if self._eliminate_candidates(cells, solved):
                    changed = True
        return changed

    def _eliminate_candidates(self, cells, solved):
        """
        Helper to remove solved values from candidate strings in given cells.
        cells: iterable of (row, col) tuples
        solved: iterable of string digits to remove
        Returns True if any candidate was changed.
        """
        changed = False
        for r, c in cells:
            if len(self.candidates[r][c]) > 1:
                before = self.candidates[r][c]
                for val in solved:
                    self.candidates[r][c] = self.candidates[r][c].replace(val, "")
                if self.candidates[r][c] != before:
                    changed = True
                    if len(self.candidates[r][c]) == 1:
                        self.board.set_cell(r, c, int(self.candidates[r][c]))
        return changed
