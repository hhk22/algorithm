


def isValid(s: str) -> bool:
    counters = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    counters_parent = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []
    for c in s:
        if c in counters:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False

            counter = stack.pop()
            if counters_parent[c] != counter:
                return False
    
    if len(stack) != 0:
        return False
    return True


s = "()[]{}"
s = "()"
print(isValid(s))
