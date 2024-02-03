class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = [0] * k
        dp[0] = arr[0]

        for i in range(1, len(arr)):
            curr_max, max_index = 0, 0
            for j in range(i, max(-1, i - k), -1):
                curr_max = max(curr_max, arr[j])
                win_size = i - j + 1
                curr_sum = curr_max * win_size
                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
                max_index = max(max_index, curr_sum + sub_sum)
            dp[i % k] = max_index
        return dp[(len(arr) - 1) % k]
