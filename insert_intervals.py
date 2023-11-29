
intervals = [[3, 5], [12, 15]]
newInterval = [6, 6]

output = [[2, 7], [8, 10], [11, 13]]
output = []


def is_overlap(itv1, itv2):
    if itv1[1] > itv2[1]:
        if itv1[0] > itv2[1]:
            return False
        else:
            return True
    else:
        if itv2[0] > itv1[1]:
            return False
        else:
            return True


triggered = False
finish = False
while (intervals):
    interval = intervals.pop(0)
    if is_overlap(newInterval, interval):
        newInterval[0] = min(newInterval[0], interval[0])
        newInterval[1] = max(newInterval[1], interval[1])
        triggered = True
    else:
        if triggered:
            output.append(interval)
            finish = True
            break

if finish is False:
    if output and newInterval[1] < output[0][0]:
        output = [newInterval] + output
    

    

if finish is False:
    if output and newInterval[1] < output[0][0]:
        output = [newInterval] + output
    else:
        output.append(newInterval)

print(output)