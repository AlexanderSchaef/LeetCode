class Solution:
    def isPalindrome(self, s: str) -> bool:
        charset = "abcdefghijklmnopqrstuvwxyz0123456789"
        new = ""
        for i, char in enumerate(s.lower()):
            if char not in charset:
                new += "|"
            else:
                new += char
        new = new.replace("|", "")
        if new == new[::-1]:
            return True
        return False
