

nums = [1, 0, -1, 0, -2, 2]
target = 0
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


def fourSum(nums, target):
    nums = sorted(nums)
    output = []
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                if sum == target and [nums[i], nums[j], nums[left], nums[right]] not in output:
                    output.append([nums[i], nums[j], nums[left], nums[right]])
                elif sum < target:
                    left += 1
                else:
                    right -= 1
    return output


result = fourSum(nums, target)
print(result)
