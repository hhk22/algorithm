

board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]

def isValidSudoku(board):
    for i in range(9):
        nums = {}
        for j in range(9):
            if board[i][j] == '.':
                continue

            if board[i][j] not in nums:
                nums[board[i][j]] = 1
            else:
                return False

    for i in range(9):
        nums = {}
        for j in range(9):
            if board[j][i] == '.':
                continue

            if board[j][i] not in nums:
                nums[board[j][i]] = 1
            else:
                return False

    for idx_i in range(0, 9, 3):
        for idx_j in range(0, 9, 3):
            nums = {}
            for i in range(idx_i, idx_i+3):
                for j in range(idx_j, idx_j+3):
                    if board[i][j] == '.':
                        continue

                    if board[i][j] not in nums:
                        nums[board[i][j]] = 1
                    else:
                        return False

    return True


rst = isValidSudoku(board)
print(rst)
