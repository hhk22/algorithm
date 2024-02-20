class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        min_dist = 9999999999999999
        min_diff = None

        for idx, num in enumerate(nums[:-2]):
            left = idx + 1
            right = len(nums) - 1

            while (left < right):
                diff = nums[idx] + nums[left] + nums[right] - target
                if diff > 0:
                    right -= 1
                elif diff < 0:
                    left += 1
                else:
                    return diff + target

                if abs(diff) < min_dist:
                    min_diff = diff
                    min_dist = abs(diff)

        return min_diff + target


s = Solution()
assert s.threeSumClosest([-1, 2, 1, -4], 2) == 2
assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
