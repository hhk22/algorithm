
class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        idx = 0
        output = 0
        while idx < len(s):
            if idx + 1 < len(s) and s[idx:idx+2] in maps:
                output += maps[s[idx:idx+2]]
                idx += 2
            else:
                output += maps[s[idx]]
                idx += 1
        return output


s = Solution()
assert s.romanToInt("III") == 3
assert s.romanToInt("LVIII") == 58
assert s.romanToInt("MCMXCIV") == 1994
