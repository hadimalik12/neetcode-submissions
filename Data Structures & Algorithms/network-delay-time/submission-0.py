class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vis = set()
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        heap = [(0, k)]
        t = 0
        while heap and len(vis) < n:
            d1, u = heapq.heappop(heap)
            if u not in vis:
                t = d1
                vis.add(u)
                for w, d2 in edges[u]:
                    if w not in vis:
                        heapq.heappush(heap, (d1 + d2, w))
        if len(vis) != n:
            return -1
        return t         

        