
class Solution:
    def twoSum(self, nums: list[int], target: int):
        maps = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            target_val = target - num
            if target_val in maps and maps[target_val] != idx:
                idx_2 = maps[target-num]
                return sorted([idx, idx_2])


s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], 6) == [1, 2]
assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
