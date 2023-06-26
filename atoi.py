

def myAtoi(s):
    pos = 0
    state = 0
    sign = 1
    value = 0
    length = len(s)

    while pos < length:
        curr = s[pos]
        if state == 0:
            if curr == " ":
                state = 0
            elif curr == "+" or curr == "-":
                state = 1
                sign = 1 if curr == '+' else -1
            elif curr.isdigit():
                state = 2
                value = value * 10 + int(curr)
            else:
                return 0

        elif state == 1:
            if curr.isdigit():
                state = 2
                value = value * 10 + int(curr)
            else:
                return 0

        elif state == 2:
            if curr.isdigit():
                state = 2
                value = value * 10 + int(curr)
            else:
                break

        else:
            return 0

        pos += 1

    value *= sign
    value = min(value, 2 ** 31 - 1)
    value = max(-(2 ** 31), value)
    return value


s = "4193 word"
print(myAtoi(s))
