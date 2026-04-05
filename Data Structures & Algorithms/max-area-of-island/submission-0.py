class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1 or (i, j) in visit:
                return 0
            else:
                visit.add((i, j))
                return (1 + dfs(i - 1, j) +
                    dfs(i, j - 1) +
                    dfs(i + 1, j) +
                    dfs(i, j + 1))

        visit = set()
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans