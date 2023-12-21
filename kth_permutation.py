'''

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"

'''


rst = []

# TimeLimit
# def make_permutation(n: int, visited: list, tmp_output):
#     for i in range(n):
#         if visited[i] is False:
#             visited[i] = True
#             make_permutation(n, visited, tmp_output + str(i+1))
#             visited[i] = False
#     if len(tmp_output) == n:
#         rst.append(tmp_output)

# n = 9
# visited = [False] * n
# make_permutation(n, visited, "")
# print("".join(rst[331987-1]))


def get_factorial(n):
    rst = 1
    for i in range(1, n+1):
        rst *= i
    return rst


def getPermutation(n: int, k: int) -> str:
    rst = ""

    def run(n, k, tot):
        nonlocal rst
        if len(tot) == 1:
            rst += tot[0]
            return

        tt = get_factorial(n-1)
        index = k // tt
        rst += tot[index]
        del tot[index]

        n -= 1
        k = k % tt
        # print(n, k, rst, index, tot)
        run(n, k, tot)

    tot = []
    for i in range(1, n+1):
        tot.append(str(i))

    run(n, k-1, tot)
    print(rst)


getPermutation(3, 0)
getPermutation(3, 1)
getPermutation(3, 2)
getPermutation(3, 3)
# getPermutation(4, 1)
# getPermutation(4, 2)
# getPermutation(4, 3)
# getPermutation(4, 4)
# getPermutation(4, 5)
# getPermutation(4, 6)
# getPermutation(4, 7)
# getPermutation(4, 8)
# getPermutation(4, 9)
# getPermutation(4, 10)
