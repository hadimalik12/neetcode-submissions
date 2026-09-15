class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x, y, count):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            
            if board[x][y] != word[count]:
                return False
            
            if count == len(word) - 1:
                return True
            
            temp = board[x][y]
            board[x][y] = "#"

            found = (dfs(x - 1, y, count + 1) or dfs(x + 1, y, count + 1) or dfs(x, y - 1, count + 1) or dfs(x, y + 1, count + 1))

            board[x][y] = temp

            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False