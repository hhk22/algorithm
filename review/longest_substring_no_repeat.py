
"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = {}
        left = 0
        max_len = 0

        for i, ch in enumerate(s):
            if ch in maps:
                left = max(left, maps[ch] + 1)
            max_len = max(max_len, i - left + 1)
            maps[ch] = i

        return max_len


s = Solution()
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring("   ") == 1
assert s.lengthOfLongestSubstring("") == 0
assert s.lengthOfLongestSubstring("c") == 1
assert s.lengthOfLongestSubstring("ab") == 2
assert s.lengthOfLongestSubstring("tmmzuxt") == 5
