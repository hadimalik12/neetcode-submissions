class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        heap = [(0,0)]
        vis = set()
        res = 0

        while len(vis) < len(points):
            cost, node = heapq.heappop(heap)
            if node in vis:
                continue
            vis.add(node)
            res += cost
            for dist, nei in adj[node]:
                if nei not in vis:
                    heapq.heappush(heap, (dist, nei))
        
        return res
