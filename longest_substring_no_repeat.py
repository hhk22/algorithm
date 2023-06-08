text = "abcabcbb"


def lengthOfLongestSubstring(text):
    record = {}
    left = 0
    max_len = 0

    for i, char in enumerate(text):
        if char in record:
            left = max(left, record[char] + 1)
        record[char] = i
        max_len = max(max_len, i - left + 1)
        print(char, max_len, left)

    return max_len

