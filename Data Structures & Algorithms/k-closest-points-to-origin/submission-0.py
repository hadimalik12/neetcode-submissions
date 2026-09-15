class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            dist = -(i[0]**2+i[1]**2)**.5
            heapq.heappush(heap, (dist, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [j[1] for j in heap]
