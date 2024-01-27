class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        last_grid = [1] + ([0] * k)
        for num in range(1, n + 1):
            curr_grid = [0] * (k + 1)
            t_count = 0
            for ran in range(k + 1):
                if ran >= num:
                    t_count -= last_grid[ran - num]
                t_count = (t_count + last_grid[ran]) % MOD
                curr_grid[ran] = t_count
            last_grid = curr_grid
        return curr_grid[-1]
