'''

Rotting Fruit
Medium
Topics
Company Tags
Hints
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:

Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4
Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1
Constraints:

1 <= grid.length, grid[i].length <= 10
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r,c) in visit:
                return 0
            q.append([r,c])
            visit.add((r,c))
            grid[r][c] = 2
            return 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
       
        if not visit:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        return -1
            return 0
        level = 0 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                print(r,c)
                out1 = bfs(r + 1, c)
                out2 = bfs(r - 1, c)
                out3 = bfs(r, c + 1)
                out4 = bfs(r, c - 1)
                print("increment")
            level += 1
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    return -1

        return level - 1
