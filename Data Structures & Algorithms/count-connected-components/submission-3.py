class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        count = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rooty] = rootx
            return True
        
        for n1, n2 in edges:
            if union(n1, n2):
                count -= 1
        
        return count