

nums = [-2, 0, 1, 1, 2]
nums = sorted(nums)
print(nums)
output = []

for i in range(len(nums) - 2):
    left = i + 1
    right = len(nums) - 1
    if nums[i] >= 0: continue
    while (left < right):
        sum = nums[i] + nums[left] + nums[right]
        if sum == 0:
            add = [nums[i], nums[left], nums[right]]
            if add not in output:
                output.append(add)
            left += 1
            right -= 1
        elif sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
