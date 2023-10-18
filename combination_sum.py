
import copy

candidates = [2, 3, 6, 7]
target = 7

# Output: [[2,2,2,2],[2,3,3],[3,5]]

output = []


def dfs(idx, temp, tot):
    if idx >= len(candidates) or tot > target:
        return

    if tot == target:
        if temp not in output:
            output.append(copy.copy(temp))
        return

    num = candidates[idx]
    temp.append(num)
    dfs(idx, temp, tot+num)
    temp.pop()
    dfs(idx+1, temp, tot)


dfs(0, [], 0)
print(output)


