
x = 1534236469
step = 10
base = -1 if x < 0 else 1
x = abs(x)


def reverse(x):
    y = 0

    while x > 0:
        quotient = x % step
        x = x // step
        y = y*10 + quotient

    y = y*base
    if (y <= -2**31 or y >= 2**31):
        return 0

    return y


reverse(x)
