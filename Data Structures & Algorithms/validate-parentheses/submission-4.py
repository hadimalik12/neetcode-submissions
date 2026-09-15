class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parentheses = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if parentheses[i] != last:
                    return False

        return len(stack) == 0