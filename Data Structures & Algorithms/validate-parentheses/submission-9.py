class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'}': '{', ']': '[', ')': '('}
        stack = []
        for i in s:
            if stack and i in hm and hm[i] == stack[-1]:
                    stack.pop()
            else:
                stack.append(i)
        
        return not stack