

nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
replace = 1

for i in range(1, len(nums)):
    if nums[i-1] != nums[i]:
        nums[replace] = nums[i]
        replace += 1

print(replace, nums)