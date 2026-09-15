class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        vis = set()

        res = 0

        def dfs(i):
            if i in vis:
                return
            
            vis.add(i)

            for nei in adj[i]:
                dfs(nei)
        
        for i in range(n):
            if i not in vis:
                dfs(i)
                res += 1
        
        return res
