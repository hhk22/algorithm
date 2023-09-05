

dividend = -1
divisor = 1

# 2147483648
output = abs(dividend) / abs(divisor)
output = output if divisor > 0 else -output
output = output if dividend > 0 else -output

output = 2**31-1 if output >= 2**31 else output
output = -2**31 if output < -2**31 else output

print(output)