
nums = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]
output = 6


ans = 0
tmp = 0
for i in nums:
    tmp += nums[i]
    ans = max(ans, tmp)
    tmp = 0 if tmp < 0 else tmp

print(ans)