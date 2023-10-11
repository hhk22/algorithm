from pprint import pprint


class Solution:

    def find_next_empty(self, puzzle):

        for r in range(9):
            for c in range(9):
                if puzzle[r][c] == ".":
                    return r, c

        return None, None

    def is_valid(self, puzzle, guess, row, col):
        row_vals = puzzle[row]
        if str(guess) in row_vals:
            return False

        col_vals = [puzzle[i][col] for i in range(9)]
        if str(guess) in col_vals:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if puzzle[r][c] == str(guess):
                    return False

        return True

    def solveSudoku(self, puzzle):
        row, col = self.find_next_empty(puzzle)

        if row is None:
            return True

        for guess in range(1, 10):
            if self.is_valid(puzzle, guess, row, col):
                puzzle[row][col] = str(guess)
                if self.solveSudoku(puzzle):
                    return True
            puzzle[row][col] = '.'

        return False


        




        






if __name__ == '__main__':
    example_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution()
    print(s.solveSudoku(example_board))
    pprint(example_board)