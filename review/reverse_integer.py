

class Solution:
    def reverse(self, x: int) -> int:
        output = 0

        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        while x > 0:
            remainder = x % 10
            x = x // 10
            output = (10 * output) + remainder

        if is_negative:
            output = -output

        if not (-2**31 < output < 2**31):
            return 0

        return output


s = Solution()
assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(1534236469) == 0
