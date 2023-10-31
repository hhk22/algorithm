
s = "aa"
p = "a"
output = False


dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
dp[0][0] = True

print(dp)