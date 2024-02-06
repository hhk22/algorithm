
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]):
        def get_med_elem(arr):
            med_idx = int(len(arr) / 2)
            if len(arr) % 2 == 0:
                return (arr[med_idx] + arr[med_idx-1]) / 2
            else:
                return arr[med_idx]

        combined_nums = []
        if not nums1 and not nums2:
            return []
        if not nums1:
            return get_med_elem(nums2)
        if not nums2:
            return get_med_elem(nums1)

        if nums1[-1] < nums2[0]:
            combined_nums.extend(nums1)
            combined_nums.extend(nums2)
        elif nums1[0] > nums2[-1]:
            combined_nums.extend(nums2)
            combined_nums.extend(nums1)
        else:
            while nums1 and nums2:
                if nums1[0] < nums2[0]:
                    combined_nums.append(nums1.pop(0))
                elif nums1[0] >= nums2[0]:
                    combined_nums.append(nums2.pop(0))

            if nums1:
                combined_nums.extend(nums1)
            elif nums2:
                combined_nums.extend(nums2)

        rst = get_med_elem(combined_nums)
        return rst


s = Solution()
assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert s.findMedianSortedArrays([], [1]) == 1
assert s.findMedianSortedArrays([], [2, 3]) == 2.5
assert s.findMedianSortedArrays([3], [1, 2, 4, 5]) == 3.0
