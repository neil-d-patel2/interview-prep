class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if word[i] != board[r][c] or r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] = '!':
                return False

            board[r][c] = '#'
            
            out = backtrack(r + 1, c, i) or
                  backtrack(r - 1, c, i) or
                  backtrack(r, c + 1, i) or
                  backtrack(r, c - 1, i) or

            board[r][c] = word[i]
            return out



        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
        
