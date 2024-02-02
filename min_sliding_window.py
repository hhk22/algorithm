

# TimeLimit
# class Solution:
#     def check(self, s_str, unique_t_str):
#         unique_s_str = {}
#         for s_ch in s_str:
#             if s_ch not in unique_s_str:
#                 unique_s_str[s_ch] = 1
#             else:
#                 unique_s_str[s_ch] += 1

#         for t_k in unique_t_str.keys():
#             if t_k not in unique_s_str:
#                 return False
#             if unique_t_str[t_k] > unique_s_str[t_k]:
#                 return False
#         return True

#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ""
#         elif t == s:
#             return s

#         unique_t_str = {}
#         for t_ch in t:
#             if t_ch not in unique_t_str:
#                 unique_t_str[t_ch] = 1
#             else:
#                 unique_t_str[t_ch] += 1

#         start_len = len(t)
#         while start_len <= len(s):
#             for i in range(len(s)-start_len+1):
#                 if self.check(s[i:i+start_len], unique_t_str):
#                     return s[i:i+start_len]
#             start_len += 1
#         return ""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        answer_key = Counter(t)
        window = {}

        valid_keys_required = len(answer_key)
        valid_keys_formed = 0

        output = float('inf'), 0, 0
        l, r = 0, 0

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in answer_key and window[char] == answer_key[char]:
                valid_keys_formed += 1

            while l <= r and valid_keys_formed == valid_keys_required:
                prev_char = s[l]

                if output[0] > (r-l+1):
                    output = (r-l+1), l, r

                window[prev_char] -= 1

                if prev_char in answer_key and window[prev_char] < answer_key[prev_char]:
                    valid_keys_formed -= 1

                l += 1

            r += 1

        return "" if output[0] == float('inf') else s[output[1]:output[2]+1]


s = "abcd"
t = "abc"
output = "abc"
sol = Solution()
rst = sol.minWindow(s, t)
print(rst)
