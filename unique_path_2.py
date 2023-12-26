

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i-1][j] != 1:
                    dp[i][j] += dp[i-1][j]
                if obstacleGrid[i][j-1] != 1:
                    dp[i][j] += dp[i][j-1]

        if obstacleGrid[-1][-1] == 1:
            return 0
        else:
            return dp[-1][-1]


obstacleGrid = [[0, 0], [1, 1], [0, 0]]
s = Solution()
rst = s.uniquePathsWithObstacles(obstacleGrid)
print(rst)
