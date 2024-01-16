

class Solution:
    def sortColors(self, arr) -> None:
        n = len(arr)
        low = 0
        high = n - 1
        curr = 0

        while curr <= high:
            if arr[curr] == 2:
                tmp = arr[high]
                arr[high] = arr[curr]
                arr[curr] = tmp
                high -= 1
            elif arr[curr] == 0:
                tmp = arr[low]
                arr[low] = arr[curr]
                arr[curr] = tmp
                low += 1
                curr += 1
            else:
                curr += 1
            print(nums)


nums = [2, 0, 2, 1, 1, 0]
s = Solution()
s.sortColors(nums)
