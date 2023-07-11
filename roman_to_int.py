

rom2int = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


def romToInt(s):
    output = 0
    curr = 0
    while curr < len(s):
        if curr < len(s) - 1 and s[curr:curr+2] in rom2int:
            output += rom2int[s[curr:curr+2]]
            curr += 2
        elif s[curr] in rom2int:
            output += rom2int[s[curr]]
            curr += 1

    return output


s = "MCMXCIV"
print(romToInt(s))

# 1994