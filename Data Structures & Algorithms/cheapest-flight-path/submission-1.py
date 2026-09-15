class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")
        dist = [inf] * n
        dist[src] = 0

        for i in range(k + 1):
            temp = dist[:]
            for s, d, w in flights:
                if dist[s] != inf and dist[s] + w < temp[d]:
                    temp[d] = dist[s] + w
            dist = temp

        if dist[dst] == inf:
            return -1
        return dist[dst]
        
        