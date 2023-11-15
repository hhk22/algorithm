

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output = [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]


n = len(matrix)
tmp = [[0] * n for _ in range(n)]
# print(output)
for i in range(n):
    for j in range(n):
        print(matrix[n-j-1][i])
        tmp[i][j] = matrix[n-j-1][i]

for i in range(n):
    for j in range(n):
        matrix[i][j] = tmp[i][j]

print(tmp)
