

nums = [1, 2, 3, 4]
output = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]


class Solution:
    def permute(self, nums):

        def backtrak(d, visited, nums, ans):
            if len(d) == len(nums):
                ans.append(d[:])
                return

            for i in range(nums):
                if not visited[i]:
                    d.append(nums[i])
                    visited[i] = True
                    backtrak(d, visited, nums, ans)
                    d.pop()
                    visited[i] = False

        visited = [0] * len(nums)
        d, ans = [], []
        backtrak(d, visited, nums, ans)
        return ans


s = Solution()
rst = s.permute(nums)
print(rst)
