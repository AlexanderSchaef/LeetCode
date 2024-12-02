class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        split = sentence.split()
        for i, e in enumerate(split):
            if e.startswith(searchWord):
                return i + 1
        return -1
