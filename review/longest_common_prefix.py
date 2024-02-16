
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common_prefix = ""
        idx = 0
        while True:
            for str in strs:
                if str == "":
                    return common_prefix

            maps = set()
            for str in strs:
                if idx >= len(str):
                    return common_prefix
                maps.add(str[idx])

            if len(maps) == 1:
                common_prefix += strs[0][idx]
                idx += 1
            else:
                return common_prefix


s = Solution()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix([""]) == ""
assert s.longestCommonPrefix(["", ""]) == ""
assert s.longestCommonPrefix(["a"]) == "a"
assert s.longestCommonPrefix(["", "b"]) == ""
