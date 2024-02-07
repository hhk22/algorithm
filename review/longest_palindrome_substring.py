
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s: str, left: int, right: int):
            if right >= len(s):
                return False

            string = ""

            while True:
                if s[left] != s[right]:
                    if string == "":
                        return False
                    return string

                if left == 0 or right == len(s) - 1:
                    return s[left:right+1]

                string = s[left:right+1]
                left -= 1
                right += 1

        def get_palindrome(s, i) -> str:
            for left, right in (i, i), (i, i+1):
                rst = check(s, left, right)
                if rst is not False:
                    if len(self.max_str) < len(rst):
                        self.max_str = rst

        self.max_str = ''
        for i in range(len(s)):
            get_palindrome(s, i)

        return self.max_str


s = Solution()
assert s.longestPalindrome("babad") == "bab"
assert s.longestPalindrome("cbbd") == "bb"
