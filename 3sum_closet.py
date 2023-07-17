

def threeSumClosest(nums, target):
    nums = sorted(nums)
    output = 999999999
    real = 0

    for i in range(len(nums) - 2):
        left = i+1
        right = len(nums) - 1

        while (left < right):
            sum = nums[i] + nums[left] + nums[right]
            if sum == target:
                return sum
            elif sum < target:
                left += 1
            else:
                right -= 1
            
            if output > abs(sum - target):
                output = abs(sum - target)
                real = sum
    
    return real


# nums = [-1, 2, 1, -4]
# -4 -1 1 2
nums = [0, 1, 2]
target = 3
print(threeSumClosest(nums, target))