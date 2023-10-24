
nums = [1, 2, 0]
# output = 3


def find(nums):
    max_val = 0
    maps = {}
    for num in nums:
        maps[num] = 1
        if num > max_val:
            max_val = num

    for num in range(1, max_val):
        if num not in maps:
            return num
    return max_val + 1

rst = find(nums)
print(rst)


