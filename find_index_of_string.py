
haystack = "sadbutsad"
needle = "sad"

ln = len(needle)
for i in range(len(haystack) - ln + 1):
    if haystack[i:i+ln] == needle:
        print(i)
        break
else:
    print(-1)