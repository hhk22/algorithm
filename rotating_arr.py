

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0


def search(nums, target):
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return -1


rst = search(nums, target)
print(rst)
