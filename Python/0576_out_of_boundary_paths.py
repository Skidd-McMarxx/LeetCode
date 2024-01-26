class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1_000_000_007
        grid = [[0] * n for _ in range(m)]

        for _ in range(1, maxMove + 1):
            tmp_grid = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    if row + 1 == m:
                        tmp_grid[row][col] = (tmp_grid[row][col] + 1) % MOD
                    else:
                        tmp_grid[row][col] = (tmp_grid[row][col] + grid[row + 1][col]) % MOD
                    if row - 1 < 0:
                        tmp_grid[row][col] = (tmp_grid[row][col] + 1) % MOD
                    else:
                        tmp_grid[row][col] = (tmp_grid[row][col] + grid[row - 1][col]) % MOD

                    if col + 1 == n:
                        tmp_grid[row][col] = (tmp_grid[row][col] + 1) % MOD
                    else:
                        tmp_grid[row][col] = (tmp_grid[row][col] + grid[row][col + 1]) % MOD
                    if col - 1 < 0:
                        tmp_grid[row][col] = (tmp_grid[row][col] + 1) % MOD
                    else:
                        tmp_grid[row][col] = (tmp_grid[row][col] + grid[row][col - 1]) % MOD
            grid = tmp_grid
        return grid[startRow][startColumn]
