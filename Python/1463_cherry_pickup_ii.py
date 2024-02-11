from itertools import product

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        delt = [-1, 0, 1]
        dp = [[0] * COLS for _ in range(COLS) ]

        for r in reversed(range(ROWS)):
            curr_dp = [[0] * COLS for _ in range(COLS)]
            for c1 in range(COLS - 1):
                for c2 in range(c1 + 1, COLS):
                    max_cher = 0
                    cher = grid[r][c1] + grid[r][c2]
                    for c1_d, c2_d in product(delt, delt):
                        nc1, nc2 = c1 + c1_d, c2 + c2_d
                        if nc1 < 0 or nc2 == COLS:
                            continue
                        max_cher = max(max_cher, cher + dp[nc1][nc2])
                    curr_dp[c1][c2] = max_cher
            dp = curr_dp
        return dp[0][-1]
