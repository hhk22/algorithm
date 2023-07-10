
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


def int_to_roman(num):
    s = ""
    char_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    for _, n in enumerate(char_list):
        quant = 0
        while True:
            print(num, quant, 'before', n)
            quant = num // rom2int[n]
            num = num - quant * rom2int[n]
            print(num, quant, 'after', n)
            if quant > 0:
                s += n * quant
            else:
                break

    return s


num = 1994
# print(rom2int['M'])
print(int_to_roman(num))
