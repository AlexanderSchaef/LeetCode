class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1
        length = len(word)
        char = word[0]
        for i in range(1, length):
            if word[i] == char and count < 9:
                count += 1
            else:
                comp += str(count) + char
                char = word[i]
                count = 1
        comp += str(count) + char
        return comp
