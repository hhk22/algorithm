

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        x_index = 0
        for i in range(1, len(matrix)):
            if target < matrix[i][0]:
                break
            x_index = i

        for i in range(len(matrix[0])):
            if target == matrix[x_index][i]:
                return True

            if target < matrix[x_index][i]:
                return False

        return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 3

s = Solution()
rst = s.searchMatrix(matrix, target)
print(rst)
