

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

replace = 0
for i in range(0, len(nums)):
    if nums[i] != val:
        nums[replace] = nums[i]
        replace += 1
print(nums)


