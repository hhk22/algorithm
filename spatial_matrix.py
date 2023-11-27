
import itertools

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
direction = ["right", "down", "left", "up"]
cycle_dir = itertools.cycle(direction)
output_mat = []

curr_dir = next(cycle_dir)


def move(i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        return (i, j)
    else:
        return "out"


curr_i = 0
curr_j = 0
output = [matrix[0][0]]
visited[0][0] = True
count = 0
count_max = len(matrix) * len(matrix[0]) - 1
while (True):
    if count == count_max:
        break

    rst = None
    if curr_dir == "right":
        rst = move(curr_i, curr_j+1)
    elif curr_dir == "down":
        rst = move(curr_i+1, curr_j)
    elif curr_dir == "left":
        rst = move(curr_i, curr_j-1)
    elif curr_dir == "up":
        rst = move(curr_i-1, curr_j)

    if rst == "out":
        curr_dir = next(cycle_dir)
    else:
        if visited[rst[0]][rst[1]] is False:
            visited[rst[0]][rst[1]] = True
            curr_i = rst[0]
            curr_j = rst[1]
            output.append(matrix[curr_i][curr_j])
            count += 1
        else:
            curr_dir = next(cycle_dir)

print(output)
