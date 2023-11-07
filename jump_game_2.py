

nums = [2, 1, 1, 1, 1]
output = 3

count = 0
idx = 0
right = 0
reach = 0
while idx < len(nums) - 1:
    reach = max(reach, idx + nums[idx])

    if idx == right:
        right = reach
        count += 1

    idx = idx + 1

print(count)

