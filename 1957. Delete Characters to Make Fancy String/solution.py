class Solution:
    def makeFancyString(self, s: str) -> str:
        final_str = ""
        for index, char in enumerate(s):
            if index == 0 or index == len(s) - 1:
                final_str += char
            elif s[index - 1] == char and char == s[index + 1]:
                pass
            else:
                final_str += char
        return final_str
