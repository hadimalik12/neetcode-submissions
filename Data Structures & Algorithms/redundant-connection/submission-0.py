class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        res = []

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
            if not union(n1, n2):
                return [n1, n2]
        

        

