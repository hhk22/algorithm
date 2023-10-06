
s = "()(((()))"
s = "()((())"
s = "()(()()"  # 3

queue = []
max_len = 0
for i in range(len(s)):
    if s[i] == '(':
        queue.append(i)
    else:
        if queue:
            index = queue.pop()
            max_len = max(2 * (i - index), max_len)

print(max_len)


def longestValidParentheses(self, s: str) -> int:
    stack = [-1]
    max_so_far = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_so_far = max(max_so_far,i - stack[-1])
    return max_so_far