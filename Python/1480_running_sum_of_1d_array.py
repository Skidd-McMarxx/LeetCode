class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        if len(nums) > 1:
            for i in range(1, len(nums)):
                nums[i] += nums[i-1]
        return nums