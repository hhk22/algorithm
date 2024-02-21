
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        output = []

        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    tot = nums[i] + nums[j] + nums[l] + nums[r]
                    if tot == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in output:
                            output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif tot < target:
                        l += 1
                    else:
                        r -= 1

        return output


s = Solution()
assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

