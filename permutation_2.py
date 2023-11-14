

nums = [1, 1, 2]
output = [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
]


class Solution:
    def permute(self, nums):

        def backtrak(d, visited, nums, ans):
            if len(d) == len(nums):
                ans.append(d[:])
                return

            for i in range(len(nums)):
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
nums.sort()
rst = s.permute(nums)
print(rst)
