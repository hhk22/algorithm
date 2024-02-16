
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:

    def intToRoman(self, num: int) -> str:
        maps = {
            1000: "M",
            900: "CM",
            500: "D",
            100: "C",
            90: "XC",
            50: "L",
            10: "X",
            9: "IV",
            5: "V",
            4: "IV",
            1: "I"
        }

        candidates = [1000, 900, 500, 100, 90, 50, 10, 9, 5, 4, 1]
        output_str = ""

        for candidate in candidates:
            quant = num // candidate
            num = num % candidate
            output_str += quant * maps[candidate]

        return output_str


s = Solution()
assert s.intToRoman(3) == "III"
assert s.intToRoman(58) == "LVIII"
assert s.intToRoman(1994) == "MCMXCIV"
