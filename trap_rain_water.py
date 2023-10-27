
height = [2, 0, 2]
output = 2

bound = 0
traps = 0
max_height = max(height)
max_idx_to_right = None
max_idx_to_left = None
for idx, num in enumerate(height):
    if num == max_height:
        max_idx_to_right = idx
        break

    if num > bound:
        bound = num

    if num < bound:
        traps += (bound - num)

bound = 0
for idx, num in enumerate(height[::-1]):
    if num == max_height:
        max_idx_to_left = len(height) - idx - 1
        break

    if num > bound:
        bound = num
    if num < bound:
        traps += (bound - num)

if max_idx_to_right != max_idx_to_left:
    for num in height[max_idx_to_right+1:max_idx_to_left]:
        traps += (max_height - num)

print(traps)

    


    







# print(max_area)