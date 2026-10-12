class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        stack.append((0, temperatures[0]))

        for i, j in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][1]:
                x, y = stack.pop()
                res[x] = i - x
            stack.append((i,j))
        
        return res
            
        

