
s = 'babad'
l, n1, n2 = len(s), 0, 1


def run_palindrome(s, i):
    max_char = ""

    for left, right in (i, i), (i, i+1):
        while left >= 0 and right < len(s):
            if (s[left] != s[right]):
                break

            if right - left + 1 > len(max_char):
                max_char = s[left:right+1]

            left -= 1
            right += 1

    return max_char


def run():
    max_char = ""

    for i in range(len(s)):
        result = run_palindrome(s, i)
        if (len(result) > len(max_char)):
            max_char = result

    print(max_char)
    return max_char


run()
