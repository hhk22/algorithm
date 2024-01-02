
a = "1010"
b = "1011"


quant = 0
a = list(a)
b = list(b)
output = ""

while (a or b):
    summation = quant
    if a and not b:
        summation += int(a.pop())
    elif not a and b:
        summation += int(b.pop())
    else:
        summation += int(a.pop()) + int(b.pop())
    
    print(summation)

    if summation >= 2:
        output = str(summation % 2) + output
        quant = 1
    else:
        output = str(summation) + output
        quant = 0


if quant:
    output = str(quant) + output

print(output)
