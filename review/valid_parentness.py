class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for ch in s:
            if ch in [')', ']', '}']:
                if not stack:
                    return False
                counter = stack.pop()
                if maps[ch] != counter:
                    return False
            else:
                stack.append(ch)
        return False if stack else True


s = Solution()
assert s.isValid('()') is True
assert s.isValid("()[]{}") is True
assert s.isValid("]") is False
