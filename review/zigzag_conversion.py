

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        maps = [[] for _ in range(numRows)]
        if numRows == 1:
            return s

        curr_idx = 0
        direction = 1

        for ch in s:
            maps[curr_idx].append(ch)
            if curr_idx == numRows - 1:
                direction = -1
            elif curr_idx == 0:
                direction = 1
            curr_idx += direction

        output_str = ""
        for map_str in maps:
            output_str += "".join(map_str)

        return output_str


s = Solution()
# assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert s.convert("ABC", 1) == "ABC"
