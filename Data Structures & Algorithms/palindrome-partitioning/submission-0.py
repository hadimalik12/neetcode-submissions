class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                if isPal(s[start:end+1]):
                    path.append(s[start:end+1])
                    dfs(end+1,path)
                    path.pop()

        def isPal(s):
            return s == s[::-1]

        dfs(0, [])
        return res
