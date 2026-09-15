class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i : [] for i in range(n)}

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visit = set()

        count = 0
        
        def dfs(i):
            if i in visit:
                return
            
            visit.add(i)

            for k in adj[i]:
                dfs(k)
            
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
            
        
        return count



