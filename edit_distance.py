
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0] * (len(word1) + 1) for _ in range(len(word2)+1)]

        for i in range(len(word1) + 1):
            matrix[0][i] = i
        for i in range(len(word2) + 1):
            matrix[i][0] = i

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j-1] == word2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    min_val = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
                    matrix[i][j] = min_val + 1

        return matrix[-1][-1]


word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
output = 10
# word1 = "horse"
# word2 = "ros"

s = Solution()
ans = s.minDistance(word1, word2)
print(ans)
