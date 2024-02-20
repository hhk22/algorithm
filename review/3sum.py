
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        output = set()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                continue
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    output.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

        new_output = []
        for item in output:
            new_output.append(list(item))
        return new_output


s = Solution()
# assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert s.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
