
string = "AB"
numRows = 1
output = []

if numRows == 1:
    print(string)

for i in range(numRows):
    output.append([])


curr = 0
delta = 1
string = list(string)

while (string):
    c = string.pop(0)
    output[curr].append(c)
    curr += delta
    if curr == numRows-1:
        delta = -1
    elif curr == 0:
        delta = 1

output_str = ""
for tt in output:
    output_str += "".join(tt)
