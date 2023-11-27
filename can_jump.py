
nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
# output = True


def canJump(nums):
    right = 0
    reach = 0
    idx = 0
    while (1):
        reach = max(reach, idx+nums[idx])

        if idx == right:
            if right == reach and reach != len(nums) - 1:
                return False
            right = reach
        
        idx += 1
        if idx == len(nums):
            return True


rst = canJump(nums)
print(rst)
