
class Solution:
    def myAtoi(self, s: str) -> int:
        def get_sign(value):
            if value is None:
                return 1
            elif value is False:
                return -1
            else:
                return 1

        def return_value(value: int, sign):
            sign = get_sign(sign)
            value = sign * value

            if -(2**31) < value < 2**31:
                return value
            elif value <= -(2**31):
                return -(2**31)
            else:  # value >= 2**31
                return 2**31 - 1

        output = 0
        sign = None
        checked_digit = False
        for ch in s:
            if ch.isdigit():
                checked_digit = True
                output = (output * 10) + int(ch)
            elif ch == " ":
                if checked_digit or sign is not None:
                    return return_value(output, sign)
                continue
            elif ch == "+":
                if sign is not None or checked_digit:
                    return return_value(output, sign)
                sign = True
            elif ch == "-":
                if sign is not None or checked_digit:
                    return return_value(output, sign)
                sign = False
            else:
                return return_value(output, sign)
        return return_value(output, sign)


s = Solution()
# assert s.myAtoi("123") == 123
# assert s.myAtoi("   -42") == -42
# assert s.myAtoi("4193 with words") == 4193
# assert s.myAtoi("+-12") == 0
# assert s.myAtoi("-91283472332") == -2147483648
# assert s.myAtoi("00000-42a1234") == 0
# assert s.myAtoi("   +0 123") == 0
# assert s.myAtoi("    -88827   5655  U") == -88827
# assert s.myAtoi("-5-") == -5
assert s.myAtoi("  +  413") == 0
