class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x[0] == "-":
            return False

        left = 0
        right = len(str_x) - 1

        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        return True


s = Solution()
assert s.isPalindrome(121) is True
assert s.isPalindrome(-123) is False
assert s.isPalindrome(10) is False
