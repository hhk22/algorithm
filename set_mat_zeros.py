
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


class Solution:
    def _fill(self, matrix, zero_index):
        for i in range(len(matrix[0])):
            matrix[zero_index[0]][i] = 0
        for i in range(len(matrix)):
            matrix[i][zero_index[1]] = 0

    def _find(self, matrix):
        zero_indexes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_indexes.append((i, j))
        return zero_indexes

    def setZeroes(self, matrix) -> None:
        zero_indexes = self._find(matrix)
        for zero_index in zero_indexes:
            self._fill(matrix, zero_index)


s = Solution()
rst = s.setZeroes(matrix)
print(rst)
