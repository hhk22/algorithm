
num = 121


def isPalindrome(x):
    left = 0
    right = len(str(x)) - 1

    s = str(x)
    while left <= right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


print(isPalindrome(num))
