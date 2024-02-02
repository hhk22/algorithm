
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.rst = []

        def run(num, acc: list):
            if len(acc) == k:
                self.rst.append(acc[:])
                return

            for i in range(num, n+1):
                acc.append(i)
                run(i + 1, acc)
                acc.pop()

        run(1, [])
        return self.rst


# n = 4
# k = 2
n = 2
k = 1

s = Solution()
rst = s.combine(n, k)
print(rst)
