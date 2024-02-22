class Solution(object):
    def generateParenthesis(self, n):
        def go_step(f_used: int, b_used: int, tmp: str):
            if f_used == b_used == self.n:
                self.output.append(tmp)
                return

            if f_used < self.n:
                go_step(f_used+1, b_used, tmp+"(")
            if f_used > b_used and b_used < self.n:
                go_step(f_used, b_used+1, tmp+")")

        self.output = []
        self.n = n
        go_step(1, 0, "(")
        return self.output


s = Solution()
assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]