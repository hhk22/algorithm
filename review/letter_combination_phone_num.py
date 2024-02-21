class Solution:
    digit2str = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits: str) -> list[str]:
        output = []
        while digits:
            digit = digits[0]
            digits = digits[1:]
            ch_list = self.digit2str[digit]

            if not output:
                output = ch_list
            else:
                new_output = []
                for ch1 in output:
                    for ch2 in ch_list:
                        new_output.append(ch1+ch2)
                output = new_output
        return output


s = Solution()
assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
