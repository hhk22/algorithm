

n = 3


def is_block(pos, rst):
    x, y = pos[0], pos[1]
    if (x-1 >= 0 and rst[x-1][y] == 0):
        return False
    elif (x+1 < n and rst[x+1][y] == 0):
        return False
    elif (y-1 >= 0 and rst[x][y-1] == 0):
        return False
    elif (y+1 < n and rst[x][y+1] == 0):
        return False
    return True


def get_next_direction(pos, direction):
    if direction == "right":
        if pos[1] + 1 < n:
            return "right"
        else:
            return "down"
    elif direction == "down":
        if pos[0] + 1 < n:
            return "down"
        else:
            return "left"
    elif direction == "left":
        if pos[1] - 1 >= 0:
            return "left"
        else:
            return "up"
    elif direction == "up":
        if pos[0] - 1 >= 0:
            return "up"
        else:
            return "right"


def check_step(pos, rst, direction):
    x, y = pos[0], pos[1]
    if direction == "right":
        if rst[x][y+1] != 0:
            return False
        else:
            return (x, y+1)
    elif direction == "up":
        if rst[x-1][y] != 0:
            return False
        else:
            return (x-1, y)
    elif direction == "down":
        if rst[x+1][y] != 0:
            return False
        else:
            return (x+1, y)
    elif direction == "left":
        if rst[x][y-1] != 0:
            return False
        else:
            return (x, y-1)


def change_direction(direction):
    if direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"
    elif direction == "up":
        return "right"


def go_step(pos, direction):
    x, y = pos[0], pos[1]
    if direction == "right":
        return (x, y+1)
    elif direction == "up":
        return (x-1, y)
    elif direction == "down":
        return (x+1, y)
    elif direction == "left":
        return (x, y-1)


def get_next_pos(pos, rst, direction):
    if is_block(pos, rst):
        return rst, "finish"

    next_direction = get_next_direction(pos, direction)
    while True:
        tmp_checked = check_step(pos, rst, next_direction)
        if tmp_checked is not False:
            break
        else:
            next_direction = change_direction(next_direction)
    pos = go_step(pos, next_direction)
    direction = next_direction

    return pos, direction


def generateMatrix(n: int):
    rst = [[0] * n for _ in range(n)]
    pos = (0, 0)
    num = 1
    rst[0][0] = num
    direction = "right"
    while True:
        pos, direction = get_next_pos(pos, rst, direction)
        if direction == "finish":
            return pos

        num += 1
        rst[pos[0]][pos[1]] = num


rst = generateMatrix(n)
print(rst)



