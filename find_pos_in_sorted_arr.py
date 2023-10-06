
nums = [1]
target = 1


def searchRange(nums, target):
    start_idx = -1
    final_idx = -1

    for idx, num in enumerate(nums):

        if target == num and start_idx == -1:
            start_idx = idx

        if target == num and start_idx != -1:
            final_idx = idx

    return [start_idx, final_idx]


rst = searchRange(nums, target)
print(rst)
