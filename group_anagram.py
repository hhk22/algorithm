

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
maps = {}

for s in strs:
    key = ''.join(sorted(s))
    if key not in maps:
        maps[key] = []
    maps[key].append(s)

print(list(maps.values()))
