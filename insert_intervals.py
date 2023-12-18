
intervals = [[3, 5], [12, 15]]
newInterval = [6, 6]

output = [[2, 7], [8, 10], [11, 13]]
output = []


def insert(intervals, newInterval):
    result = []

    for i in range(len(intervals)):
        if newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        elif newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        else:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
            ]
    result.append(newInterval)
    return result


rst = insert(intervals, newInterval)
print(rst)
