
from typing import List
# leetcode: problem4
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_arr = sorted(nums1 + nums2)

        mid = len(combined_arr) // 2
        if len(combined_arr) % 2 != 0:
            return float(combined_arr[mid])
        else:
            return (combined_arr[mid-1]+combined_arr[mid])/2


s = Solution()
nums1 = [1, 3]
nums2 = [2]
target = 2
assert target == s.findMedianSortedArrays(nums1, nums2)

