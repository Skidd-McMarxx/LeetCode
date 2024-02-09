class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[n] for n in nums]
        long_i = 0
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            long_i = i if len(dp[i]) > len(dp[long_i]) else long_i
        return dp[long_i]
