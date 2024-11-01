class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
            return False
        open_char = "([{"
        close_char = ")]}"
        stack = []
        for char in s:
            if char in open_char:
                stack.append(char)
            elif char in close_char:
                if stack:
                    pop = stack.pop()
                else:
                    return False
                if pop == "{" and not char == "}":
                    return False
                elif pop == "(" and not char == ")":
                    return False
                elif pop == "[" and not char == "]":
                    return False
        if not stack:
            return True
        return False



