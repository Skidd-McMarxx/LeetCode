class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))
        for tar in range(1, n + 1):
            sq = 1
            while sq ** 2 <= tar:
                dp[tar] = min(dp[tar], 1 + dp[tar - sq ** 2])
                sq += 1
        return dp[n]
