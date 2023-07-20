

dictionary = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
}


def update(digit, result):
    if not result:
        for character in dictionary[digit]:
            result.append(character)
        return result
    
    new_result = []
    while result:
        tmp = result.pop()
        for chracter in dictionary[digit]:
            new_result.append(tmp + chracter)
    return new_result

def combination_phone_number(digits):
    result = []
    for digit in digits:
        result = update(digit, result)
    return result


digits = "23"
output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(combination_phone_number(digits))