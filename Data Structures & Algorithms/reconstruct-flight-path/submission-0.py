class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for i, j in tickets:
            heapq.heappush(adj[i], j)
        
        res = []

        def dfs(start):
            while adj[start]:
                dest = heapq.heappop(adj[start])
                dfs(dest)
            res.append(start)
        

        dfs("JFK")
        return res[::-1]
            




            
            