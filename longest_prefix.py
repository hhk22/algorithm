
def longestCommonPrefix(strs) -> str:
    output = ""
    i = 0
    while True:
        before = ""
        for str in strs:
            if i >= len(str): 
                return output

            if not before:
                before = str[i]
            if before != str[i]:
                return output
        output += before
        i += 1


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
