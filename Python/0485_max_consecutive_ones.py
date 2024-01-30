class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_total, count = 0, 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                max_total = max(max_total, count)
                count = 0
        max_total = max(max_total, count)
        return max_total
