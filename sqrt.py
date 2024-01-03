
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            double = mid * mid
            if double == x:
                return mid
            elif double < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


s = Solution()
rst = s.mySqrt(8)
print(rst)
