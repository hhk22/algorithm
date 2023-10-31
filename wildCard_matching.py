
s = "adceb"
p = "*a*b"

output = False


dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
dp[0][0] = True

for i in range(1, len(p) + 1):
    if p[i-1] == '*':
        dp[0][i] = dp[0][i-1]

for i in range(1, len(s) + 1):
    for j in range(1, len(p) + 1):
        if s[i-1] == p[j-1] and dp[i-1][j-1]:
            dp[i][j] = True
        elif p[j-1] == '*':
            dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]
        elif p[j-1] == '?':
            dp[i][j] = dp[i-1][j-1]

print(dp)
print(dp[-1][-1])
