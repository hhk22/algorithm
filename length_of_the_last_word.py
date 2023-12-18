

s = "Hello World"
output = 5


def lengthOfLastWord(input_str: str):
    words = input_str.strip().split()
    return len(words[-1])


rst = lengthOfLastWord(s)
print(rst)
