class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        count = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            cell = q.popleft()
            x, y, count = cell[0], cell[1], cell[2]

            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = min(grid[nr][nc], count + 1)
                    q.append((nr, nc, count + 1))
    
