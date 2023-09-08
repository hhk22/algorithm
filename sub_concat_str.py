
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]

# output = [13]
output = []
idx = 0
word_len = len(words[0])


def check(word_list, cand_dict, word_len):
    print(word_list, cand_dict)
    for i in range(0, len(word_list), word_len):
        word = word_list[i:i+word_len]
        print(word)
        if word not in cand_dict:
            return False
        if cand_dict[word] == 0:
            return False
        cand_dict[word] -= 1
    return True


while idx + (word_len * len(words)) <= len(s):
    tmp = {}
    for val in words:
        if val not in tmp:
            tmp[val] = 1
        else:
            tmp[val] += 1

    result = check(s[idx: idx + (word_len * len(words))], tmp, word_len)

    if result is True:
        output.append(idx)

    idx += 1

print(output)
