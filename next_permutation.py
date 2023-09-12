
arr = [1, 3, 2]
# 2, 1, 3


def next_permutation(arr):
    if len(arr) <= 2:
        return arr.reverse()

    pointer = len(arr) - 2
    while pointer >= 0:
        if arr[pointer] < arr[pointer+1]:
            break
        pointer -= 1

    if pointer == -1:
        return arr.reverse()

    for x in range(len(arr) - 1, pointer, -1):
        if arr[pointer] < arr[x]:
            arr[pointer], arr[x] = arr[x], arr[pointer]
            break

    arr[pointer+1:] = reversed(arr[pointer+1:])
    return arr


next_permutation(arr)
print(arr)
