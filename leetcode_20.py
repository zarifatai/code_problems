class Solution:
    def is_valid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif len(stack) != 0 and brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) != 0:
            return False
        return True

    def is_valid_2(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            elif len(stack) == 0 or brackets[stack.pop()] != char:
                return False
        return len(stack) == 0
