class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = tokens[::-1]
        operands = ['+', '-', '/', '*']
        tmp = []

        while len(stack):
            if stack[-1] not in operands:
                tmp.append(int(stack.pop()))
            else:
                i = stack.pop()
                if i == '+':
                    x = tmp.pop()
                    y = tmp.pop()
                    tmp.append(y+x)
                elif i == '-':
                    x = tmp.pop()
                    y = tmp.pop()
                    tmp.append(y-x)
                elif i == '/':
                    x = tmp.pop()
                    y = tmp.pop()
                    tmp.append(int(y/x))
                elif i == '*':
                    x = tmp.pop()
                    y = tmp.pop()
                    tmp.append(y*x)
        
        return tmp.pop()



