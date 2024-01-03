class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0, 2, 3]
        for i in range(3, n):
            stairs.append(stairs[i-2] + stairs[i-1])

        return stairs[i]


s = Solution()
rst = s.climbStairs(5)
print(rst)
