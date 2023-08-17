output = []


def generate(n, result, open_count, closed_count):
    if closed_count > open_count:
        return

    if open_count == n and closed_count == n:
        output.append(result)
        return

    if open_count < n:
        generate(n, result + '(', open_count+1, closed_count)

    if closed_count < open_count:
        generate(n, result + ')', open_count, closed_count+1)


generate(3, '', 0, 0)
print(output)
