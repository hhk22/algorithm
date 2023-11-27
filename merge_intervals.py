

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
right = None
output = []
intervals = sorted(intervals, key=lambda x: x[0])

while (intervals):
    candidate = intervals.pop(0)
    if not output:
        output.append(candidate)
        right = candidate[1]
    else:
        if candidate[0] <= right:
            tmp = output.pop()
            tmp[0] = min(tmp[0], candidate[0])
            tmp[1] = max(tmp[1], candidate[1])
            output.append(tmp)
            right = tmp[1]
        else:
            output.append(candidate)
            right = candidate[1]

print(output)
