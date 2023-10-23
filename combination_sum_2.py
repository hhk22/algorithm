
import copy

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30
output = []


def dfs(idx, temp, tot):
    if tot == target:
        if temp not in output:
            output.append(copy.copy(temp))
        return

    if idx >= len(candidates) or tot > target:
        return
    
    temp.append(candidates[idx])
    dfs(idx+1, temp, tot + candidates[idx])
    
    temp.pop()
    while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
        idx+=1

    dfs(idx+1, temp, tot)


candidates.sort()
dfs(0, [], 0)
print(output)