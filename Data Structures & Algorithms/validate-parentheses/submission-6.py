class Solution:
    def isValid(self, s: str) -> bool:
        hm = {']': '[', ')': '(', '}': '{'}
        stack = []

        for i in s:
            if i not in hm:
                stack.append(i)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if hm[i] == x:
                    continue
                else:
                    return False
        
        return not stack
        

            