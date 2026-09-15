class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while heap:
            currmax, x, y = heapq.heappop(heap)

            if x == n-1 and y == n-1:
                return currmax
            
            if (x, y) not in vis:
                vis.add((x,y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        heapq.heappush(heap, (max(currmax, grid[nx][ny]), nx, ny))
            
            