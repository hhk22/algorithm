

import copy

n = 5
output = [
    ["Q....","..Q..","....Q",".Q...","...Q."],
    ["Q....","...Q.",".Q...","....Q","..Q.."],
    [".Q...","...Q.","Q....","..Q..","....Q"],
    [".Q...","....Q","..Q..","Q....","...Q."],
    ["..Q..","Q....","...Q.",".Q...","....Q"],
    ["..Q..","....Q",".Q...","...Q.","Q...."],
    ["...Q.","Q....","..Q..","....Q",".Q..."],
    ["...Q.",".Q...","....Q","..Q..","Q...."],
    ["....Q",".Q...","...Q.","Q....","..Q.."],
    ["....Q","..Q..","Q....","...Q.",".Q..."]
] 

output = []


def _fill(visited, row, col):
    visited = copy.deepcopy(visited)


    for i in range(n):
        visited[row][i] = True
        visited[i][col] = True

        if 0 <= row-i < n and 0 <= col-i < n:
            visited[row-i][col-i] = True
        if 0 <= row+i < n and 0 <= col+i < n:
            visited[row+i][col+i] = True
        if 0 <= row-i < n and 0 <= col+i < n:
            visited[row-i][col+i] = True
        if 0 <= row+i < n and 0 <= col-i < n:
            visited[row+i][col-i] = True

    return visited


def dfs(q_map, visited, n_row):
    if n_row == n:
        output.append(q_map)
        print(q_map)
        return
    
    for i in range(n):
        if visited[n_row][i] is False:
            new_visited = _fill(visited, n_row, i)
            tmp = ["."] * n
            tmp[i] = "Q"
            dfs(q_map + ["".join(tmp)], new_visited, n_row+1)

for i in range(n):
    tmp = ["."] * n
    tmp[i] = "Q"
    q_map = ["".join(tmp)]

    visited = [[False] * n for _ in range(n)]
    visited = _fill(visited, 0, i)

    dfs(q_map, visited, 1)



# print(output)
