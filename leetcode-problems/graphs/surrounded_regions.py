'''

Surrounded Regions
Medium
Topics
Company Tags
Hints
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:



Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.


Example 2:

Input: board = [["X"]]

Output: [["X"]]
Constraints:

1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.

'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0]) 
        visit = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O' or (r,c) in visit:
                return
        
            board[r][c] = 'T'
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                        dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'




        
