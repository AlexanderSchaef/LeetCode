class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        found = False
        length = 0
        max_length = 1
        max_length_string = ""
        if s == "":
            return 0
        for i, char in enumerate(s):
            sub = char
            length = 1
            for i in range(i+1, len(s)):
                if s[i] not in sub:
                    sub = sub + s[i]
                    length = length + 1
                    if length > max_length:
                        max_length_string = sub
                        max_length = length
                elif s[i] in sub:
                    break
        return max_length
