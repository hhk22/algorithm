num1 = "123"
num2 = "12"

output = "1476"

if len(num1) >= len(num2):
    t1 = num1
    t2 = num2
else:
    t1 = num2
    t2 = num1

t1 = t1[::-1]
t2 = t2[::-1]

output = 0
big_step = 0
for n2 in t2:
    step = 10 ** big_step
    quant = 0
    for n1 in t1:
        number = int(n1) * int(n2)
        remainder = number % 10
        output += step * (remainder + quant)
        quant = number // 10
        step *= 10
    output += (step * quant)
    big_step += 1


