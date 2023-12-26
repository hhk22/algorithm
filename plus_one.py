
def plusOne(digits):
    number = 0
    weight = 1
    while digits:
        number += (digits.pop() * weight)
        weight *= 10

    number += 1
    output = []
    for s in str(number):
        output.append(int(s))

    return output


digits = [1, 2, 3]
rst = plusOne(digits)
print(rst)
