

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_p = len(p)
        len_s = len(s)

        dp = [[False] * (len_p+1) for _ in range(len_s+1)]
        dp[0][0] = True

        for idx in range(1, len_p+1):
            if p[idx-1] == "*":
                dp[0][idx] = dp[0][idx-2]

        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[-1][-1]


s = Solution()
# assert s.isMatch("aa", "a") is False
# assert s.isMatch("aa", "a*") is True
# assert s.isMatch("ab", ".*") is True
assert s.isMatch("a", ".*..a*") is False
